define(['app', 'app/devices/Devices.js'], function(app) {
    var addGroupModal = {
        templateUrl: 'app/zigbee2mqtt/groupCreateModal.html',
        controllerAs: '$ctrl',
        controller: function($scope, zigbee2mqtt) {
            var $ctrl = this;

            $ctrl.createGroup = function() {
                $ctrl.isSaving = true;

                zigbee2mqtt.sendRequest('group_add', {
                    id: $ctrl.groupId,
                    friendly_name: $ctrl.groupName,
                }).then(function() {
                    $scope.$close();
                });
            }
        }
    };

    var addDeviceToGroupModal = {
        templateUrl: 'app/zigbee2mqtt/groupAddDeviceModal.html',
        controllerAs: '$ctrl',
        controller: function($scope, zigbee2mqtt) {
            var $ctrl = this;
            $ctrl.addDevice = addDevice;
            $ctrl.devices = $scope.zigbeeDevices;

            function addDevice() {
                $ctrl.isSaving = true;

                zigbee2mqtt.sendRequest('group_include', {
                    group: $scope.group,
                    device: $ctrl.subDevice ? [$ctrl.device, $ctrl.subDevice].join('/') : $ctrl.device,
                }).then(function() {
                    $scope.$close();
                });
            }
        }
    };

    app.component('zigbee2mqttGroups', {
        bindings: {
            groups: '<',
            zigbeeDevices: '<',
            domoticzDevices: '<',
            onUpdate: '&',
            onUpdateDomoticzDevice: '&',
        },
        templateUrl: 'app/zigbee2mqtt/groups.html',
        controller: Zigbee2MqttGroupsController
    });

    app.component('zigbee2mqttGroupsTable', {
        bindings: {
            groups: '<',
            onSelect: '&',
            onUpdate: '&',
        },
        template: '<table id="zigbee2mqtt-groups-table" class="display" width="100%"></table>',
        controller: Zigbee2MqttGroupsTableController,
    });

    app.component('zigbee2mqttGroupDevicesTable', {
        bindings: {
            group: '<',
            devices: '<',
            onUpdate: '&',
        },
        template: '<table id="zigbee2mqtt-group-devices-table" class="display" width="100%"></table>',
        controller: Zigbee2MqttGroupDevicesTableController,
    });

    function Zigbee2MqttGroupsController($scope, $uibModal) {
        var $ctrl = this;

        $ctrl.addGroup = addGroup;
        $ctrl.selectZigbeeGroup = selectZigbeeGroup;
        $ctrl.addDeviceToGroup = addDeviceToGroup;

        $ctrl.$onChanges = function(changes) {
            if (changes.groups && $ctrl.selectedGroup) {
                var group = $ctrl.groups.find(function(group) {
                    return group.ID === $ctrl.selectedGroup.ID
                });

                $ctrl.selectZigbeeGroup(group);
            }

            if (changes.domoticzDevices && $ctrl.selectedGroup) {
                $ctrl.selectZigbeeGroup($ctrl.selectedGroup);
            }
        };

        function addGroup() {
            $uibModal
                .open(Object.assign({}, addGroupModal)).result
                .then($ctrl.onUpdate);
        }

        function addDeviceToGroup() {
            var scope = $scope.$new(true);
            scope.group = $ctrl.selectedGroup.friendly_name;
            scope.zigbeeDevices = $ctrl.zigbeeDevices;

            $uibModal.open(Object.assign({ scope: scope }, addDeviceToGroupModal)).result
                .then($ctrl.onUpdate);
        }

        function selectZigbeeGroup(group) {
            $ctrl.selectedGroup = group;

            if (group) {
                $ctrl.selectedGroupDevices = $ctrl.selectedGroup.devices.map(function(device) {
                    var zigbeeDevice = $ctrl.zigbeeDevices.find(function(zigbeeDevice) {
                        return device.indexOf(zigbeeDevice.ieeeAddr) === 0
                    });

                    return Object.assign({ binding: device }, zigbeeDevice);
                });

                $ctrl.associatedDevices = $ctrl.domoticzDevices.filter(function(device) {
                    return device.ID.indexOf(group.friendly_name + '_') === 0;
                });
            } else {
                $ctrl.associatedDevices = [];
                $ctrl.selectedGroupDevices = [];
            }
        }
    }

    function Zigbee2MqttGroupsTableController($element, $scope, $timeout, bootbox, dataTableDefaultSettings, zigbee2mqtt) {
        var $ctrl = this;
        var table;

        $ctrl.$onInit = function() {
            table = $element.find('table').dataTable(Object.assign({}, dataTableDefaultSettings, {
                order: [[0, 'asc']],
                columns: [
                    { title: $.t('ID'), width: '70px', data: 'ID' },
                    { title: $.t('Friendly Name'), data: 'friendly_name' },
                    {
                        title: '',
                        className: 'actions-column',
                        width: '40px',
                        data: 'ieeeAddr',
                        orderable: false,
                        render: actionsRenderer
                    },
                ],
            }));

            table.on('click', '.js-remove', function() {
                var row = table.api().row($(this).closest('tr')).data();

                bootbox.confirm('Are you sure you want to delete this zigbee group?')
                    .then(function() {
                        return zigbee2mqtt.sendRequest('group_remove', row.friendly_name);
                    })
                    .then(function() {
                        $ctrl.onUpdate();
                    });

                $scope.$apply();
                return false;
            });

            table.on('select.dt', function(event, row) {
                $ctrl.onSelect({ group: row.data() });
                $scope.$apply();
            });

            table.on('deselect.dt', function() {
                //Timeout to prevent flickering when we select another item in the table
                $timeout(function() {
                    if (table.api().rows({ selected: true }).count() > 0) {
                        return;
                    }

                    $ctrl.onSelect({ group: null });
                });

                $scope.$apply();
            });

            render($ctrl.groups);
        };

        $ctrl.$onChanges = function(changes) {
            if (changes.groups) {
                render($ctrl.groups);
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

        function actionsRenderer() {
            var actions = [];
            actions.push('<button class="btn btn-icon js-remove" title="' + $.t('Remove') + '"><img src="../../images/delete.png" /></button>');
            return actions.join('&nbsp;');
        }
    }

    function Zigbee2MqttGroupDevicesTableController($element, $scope, bootbox, dataTableDefaultSettings, zigbee2mqtt) {
        var $ctrl = this;
        var table;

        $ctrl.$onInit = function() {
            table = $element.find('table').dataTable(Object.assign({}, dataTableDefaultSettings, {
                order: [[0, 'asc']],
                paging: false,
                select: false,
                columns: [
                    { title: $.t('Friendly Name'), data: 'friendly_name' },
                    { title: $.t('Binding'), width: '170px', data: 'binding' },
                    { title: $.t('Model'), data: 'model' },
                    { title: $.t('Description'), data: 'description' },
                    {
                        title: '',
                        className: 'actions-column',
                        width: '40px',
                        data: 'ieeeAddr',
                        orderable: false,
                        render: actionsRenderer
                    },
                ],
            }));

            table.on('click', '.js-remove', function() {
                var row = table.api().row($(this).closest('tr')).data();

                bootbox.confirm('Are you sure you want to exclude this device from zigbee group?')
                    .then(function() {
                        return zigbee2mqtt.sendRequest('group_exclude', {
                            group: $ctrl.group.friendly_name,
                            device: row.binding
                        });
                    })
                    .then(function() {
                        $ctrl.onUpdate();
                    });

                $scope.$apply();
                return false;
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

        function actionsRenderer() {
            var actions = [];
            actions.push('<button class="btn btn-icon js-remove" title="' + $.t('Remove') + '"><img src="../../images/delete.png" /></button>');
            return actions.join('&nbsp;');
        }
    }
});