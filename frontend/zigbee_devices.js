define(['app', 'luxon', 'devices/Devices'], function(app, luxon) {
    var DateTime = luxon.DateTime;

    var renameDeviceModal = {
        templateUrl: 'app/zigbee2mqtt/deviceRenameModal.html',
        controllerAs: '$ctrl',
        controller: function($scope, zigbee2mqtt) {
            var $ctrl = this;
            $ctrl.oldName = $scope.device;
            $ctrl.newName = $scope.device;

            $ctrl.renameDevice = function() {
                $ctrl.isSaving = true;

                zigbee2mqtt.sendRequest('device_rename', {
                    old: $ctrl.oldName,
                    new: $ctrl.newName
                }).then(function() {
                    $scope.$close();
                });
            }
        }
    };

    var setDeviceStateModal = {
        templateUrl: 'app/zigbee2mqtt/setDeviceStateModal.html',
        controllerAs: '$ctrl',
        controller: function($scope, zigbee2mqtt) {
            var $ctrl = this;
            $ctrl.state = '{}';
            $ctrl.topic = $scope.device + '/set';

            $ctrl.setState = function() {
                $ctrl.isSaving = true;

                zigbee2mqtt.sendRequest('device_set', {
                    topic: $ctrl.topic,
                    state: JSON.parse($ctrl.state)
                }).then(function() {
                    $scope.$close();
                });
            }
        }
    };

    var deviceFirmwareUpdateModal = {
        templateUrl: 'app/zigbee2mqtt/deviceFirmwareUpdateModal.html',
    };

    app.component('zigbee2mqttDevices', {
        bindings: {
            zigbeeDevices: '<',
            domoticzDevices: '<',
            onUpdate: '&',
            onUpdateDomoticzDevice: '&',
        },
        templateUrl: 'app/zigbee2mqtt/devices.html',
        controller: Zigbee2MqttDevicesController
    });

    app.component('zigbee2mqttDevicesTable', {
        bindings: {
            devices: '<',
            onSelect: '&',
            onUpdate: '&'
        },
        template: '<table id="zigbee2mqtt-devices" class="display" width="100%"></table>',
        controller: Zigbee2MqttDevicesTableController,
    });

    function Zigbee2MqttDevicesController() {
        var $ctrl = this;

        $ctrl.selectZigbeeDevice = selectZigbeeDevice;

        $ctrl.$onInit = function() {
            $ctrl.associatedDevices = []
        };

        $ctrl.$onChanges = function(changes) {
            if (changes.domoticzDevices) {
                $ctrl.selectZigbeeDevice($ctrl.selectedZigbeeDevice)
            }
        };

        function selectZigbeeDevice(zigbeeDevice) {
            $ctrl.selectedZigbeeDevice = zigbeeDevice;

            if (!zigbeeDevice) {
                $ctrl.associatedDevices = []
            } else {
                $ctrl.associatedDevices = $ctrl.domoticzDevices.filter(function(device) {
                    return device.ID.indexOf(zigbeeDevice.ieeeAddr) === 0;
                });
            }
        }
    }

    function Zigbee2MqttDevicesTableController($element, $scope, $timeout, $uibModal, zigbee2mqtt, bootbox, dzSettings, dataTableDefaultSettings) {
        var $ctrl = this;
        var table;

        $ctrl.$onInit = function() {
            table = $element.find('table').dataTable(Object.assign({}, dataTableDefaultSettings, {
                order: [[0, 'asc']],
                columns: [
                    { title: 'Friendly Name', data: 'friendly_name' },
                    { title: 'Model', data: 'model' },
                    { title: 'Description', data: 'description' },
                    { title: 'Type', width: '150px', data: 'type' },
                    { title: 'IEEE Address', width: '170px', data: 'ieeeAddr' },
                    { title: 'Last Seen', data: 'lastSeen', width: '150px', render: dateRenderer },
                    {
                        title: '',
                        className: 'actions-column',
                        width: '80px',
                        data: 'ieeeAddr',
                        orderable: false,
                        render: actionsRenderer
                    },
                ],
            }));

            table.on('click', '.js-rename-device', function() {
                var row = table.api().row($(this).closest('tr')).data();
                var scope = $scope.$new(true);
                scope.device = row.friendly_name;

                $uibModal
                    .open(Object.assign({ scope: scope }, renameDeviceModal)).result
                    .then($ctrl.onUpdate);

                $scope.$apply();
                return false;
            });

            table.on('click', '.js-check-updates', function() {
                var device = table.api().row($(this).closest('tr')).data();

                zigbee2mqtt.sendRequest('device_get_ota_update_status', device.friendly_name)
                    .then(function(message) {
                        return bootbox.confirm([
                            message + '. An update typically takes +- 10 minutes.',
                            'While a device is updating a lot of traffic is generated on the network, therefore it is not recommend to execute multiple updates at the same time.',
                            'Do you want to update the device now?'
                        ].join('<br/><br />'))
                    })
                    .then(function() {
                        var scope = $scope.$new(true);
                        scope.progress = 0;
                        scope.message = 'Waiting for status update...'

                        var onUpdate = function(data) {
                            Object.assign(scope, data)
                        }

                        $uibModal.open(Object.assign({ scope: scope }, deviceFirmwareUpdateModal));

                        return zigbee2mqtt.sendRequest('device_ota_update', device.friendly_name)
                            .then(null, null, onUpdate) // Show progress to browser console
                    })
                    .then(function(message) {
                        bootbox.alert(message)
                    })
                    .catch(function(error) {
                        bootbox.alert(error);
                    });

                $scope.$apply();
                return false;
            });

            table.on('click', '.js-set-state', function() {
                var row = table.api().row($(this).closest('tr')).data();
                var scope = $scope.$new(true);
                scope.device = row.friendly_name;

                $uibModal.open(Object.assign({ scope: scope }, setDeviceStateModal));
                $scope.$apply();
                return false;
            });

            table.on('select.dt', function(event, row) {
                $ctrl.onSelect({ device: row.data() });
                $scope.$apply();
            });

            table.on('deselect.dt', function() {
                //Timeout to prevent flickering when we select another item in the table
                $timeout(function() {
                    if (table.api().rows({ selected: true }).count() > 0) {
                        return;
                    }

                    $ctrl.onSelect({ device: null });
                });

                $scope.$apply();
            });

            render($ctrl.devices);
        };

        $ctrl.$onChanges = function(changes) {
            if (changes.devices) {
                render($ctrl.devices);
            }
        };

        function render(items) {
            if (!table || !items) {
                return;
            }

            table.api().clear();
            table.api().rows
                .add(items)
                .draw();
        }

        function dateRenderer(data, type, row) {
            if (type === 'sort' || type === 'type' || !Number.isInteger(data)) {
                return data;
            }

            return DateTime.fromMillis(data).toFormat(dzSettings.serverDateFormat);
        }

        function actionsRenderer(data, type, row) {
            var actions = [];
            var delimiter = '<img src="../../images/empty16.png" width="16" height="16" />';

            actions.push('<button class="btn btn-icon js-check-updates" title="' + $.t('Check for OTA firmware updates') + '"><img src="images/hardware.png" /></button>');
            actions.push(delimiter)
            actions.push('<button class="btn btn-icon js-set-state" title="' + $.t('Set State') + '"><img src="images/events.png" /></button>');
            actions.push('<button class="btn btn-icon js-rename-device" title="' + $.t('Rename Device') + '"><img src="images/rename.png" /></button>');
            return actions.join('&nbsp;');
        }
    }
});