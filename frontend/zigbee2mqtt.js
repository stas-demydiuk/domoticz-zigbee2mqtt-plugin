define([
    'app',
    'luxon',
    '../templates/zigbee2mqtt/viz',
    '../templates/zigbee2mqtt/viz.full.render',
    '../templates/zigbee2mqtt/leaflet'
],
function(app, luxon, Viz, vizRenderer, leaflet) {
    var viz = new Viz(vizRenderer);
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

    app.component('zigbee2mqttPlugin', {
        templateUrl: 'app/zigbee2mqtt/index.html',
        controller: Zigbee2MqttPluginController
    });

    app.component('zigbee2mqttDevicesTable', {
        bindings: {
            devices: '<',
            onUpdate: '&'
        },
        template: '<table id="zigbee2mqtt-devices" class="display" width="100%"></table>',
        controller: Zigbee2MqttDevicesTableController,
    });

    app.factory('zigbee2mqtt', function($q, $rootScope, domoticzApi) {
        var deviceIdx = 0;
        var requestsCount = 0;
        var requestsQueue = [];

        $rootScope.$on('device_update', function(e, device) {
            if (device.idx === deviceIdx) {
                handleResponse(JSON.parse(device.Data))
            }
        });

        return {
            setControlDeviceIdx: setControlDeviceIdx,
            sendRequest: sendRequest,
        };

        function setControlDeviceIdx(idx) {
            deviceIdx = idx;
        }

        function sendRequest(command, params) {
            return $q(function(resolve, reject) {
                var requestId = ++requestsCount;

                var requestInfo = {
                    requestId: requestId,
                    callback: resolve
                };

                requestsQueue.push(requestInfo);

                domoticzApi.sendCommand('udevice', {
                    idx: deviceIdx,
                    svalue: JSON.stringify({
                        type: 'request',
                        requestId: requestId,
                        command: command,
                        params: params || {}
                    })
                }).catch(reject);
            })
        }

        function handleResponse(data) {
            if (data.type !== 'response') {
                return;
            }

            var requestIndex = requestsQueue.findIndex(function(item) {
                return item.requestId === data.requestId;
            });

            if (requestIndex === -1) {
                return;
            }

            var requestInfo = requestsQueue[requestIndex];
            requestInfo.callback(data.payload);
            requestsQueue.splice(requestIndex, 1);
        }
    });

    function Zigbee2MqttPluginController($scope, $element, domoticzApi, dzNotification, zigbee2mqtt) {
        var $ctrl = this;

        $ctrl.getVersionString = getVersionString;
        $ctrl.renderNetworkMap = renderNetworkMap;
        $ctrl.fetchZigbeeDevices = fetchZigbeeDevices;
        $ctrl.togglePermitJoin = togglePermitJoin;

        $ctrl.$onInit = function() {
            $ctrl.devices = [];
            refreshDevices();
        };

        function fetchZigbeeDevices() {
            zigbee2mqtt.sendRequest('devices_get').then(function(devices) {
                $ctrl.zigbeeDevices = devices.map(function(device) {
                    return Object.assign({
                        model: null,
                    }, device, {
                        lastSeen: device.lastSeen || 'N/A'
                    });
                });
            });
        }

        function fetchControllerInfo() {
            return zigbee2mqtt.sendRequest('bridge_getstatus').then(function(data) {
                $ctrl.controllerInfo = data;
            });
        }

        function renderNetworkMap() {
            if ($ctrl.isMapLoaded) {
                return;
            }

            zigbee2mqtt.sendRequest('network_map').then(renderSvg).then(function() {
                $ctrl.isMapLoaded = true;
            });
        }

        function togglePermitJoin() {
            var value = $ctrl.controllerInfo.permit_join.toString();

            return zigbee2mqtt.sendRequest('bridge_set_permitjoin', value).then(function(data) {
                $ctrl.permitJoin = data.permit_join;

                var message = $ctrl.permitJoin
                    ? 'New devices are now allowed to join the network'
                    : 'New devices are not allowed to join the network';

                dzNotification.show(message, 2500)
            })
        }

        function getVersionString() {
            return `v.${$ctrl.controllerInfo.version} (${$ctrl.controllerInfo.coordinator.type} ${$ctrl.controllerInfo.coordinator.meta.revision})`;
        }

        function renderSvg(svgData) {
            var vizOptions = {
                engine: 'circo',
            };

            return viz.renderSVGElement(svgData, vizOptions)
                .then(function(element) {
                    var map = leaflet.map($element.find('#image-map')[0], {
                        center: [0, 0],
                        zoom: 1,
                        crs: L.CRS.Simple
                    });

                    var bounds = [[0, 0], [-500, 500]];

                    leaflet.svgOverlay(element, bounds).addTo(map)
                })
        }

        function refreshDevices() {
            domoticzApi.sendRequest({
                type: 'devices',
                displayhidden: 1,
                filter: 'all',
                used: 'all'
            })
                .then(domoticzApi.errorHandler)
                .then(function(response) {
                    if (response.result !== undefined) {
                        $ctrl.devices = response.result
                            .filter(function(device) {
                                return device.HardwareType === 'Zigbee2MQTT'
                            });

                        $ctrl.apiDevice = $ctrl.devices.find(function(device) {
                            return device.Unit === 255
                        });

                        zigbee2mqtt.setControlDeviceIdx($ctrl.apiDevice.idx);

                        fetchControllerInfo().then(fetchZigbeeDevices);
                    } else {
                        $ctrl.devices = [];
                    }
                });
        }
    }

    function Zigbee2MqttDevicesTableController($element, $scope, $uibModal, zigbee2mqtt, dzSettings, dataTableDefaultSettings) {
        var $ctrl = this;
        var table;

        $ctrl.$onInit = function() {
            table = $element.find('table').dataTable(Object.assign({}, dataTableDefaultSettings, {
                order: [[0, 'asc']],
                columns: [
                    { title: 'Friendly Name', data: 'friendly_name' },
                    { title: 'Model', data: 'model' },
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
            });

            table.on('click', '.js-set-state', function() {
                var row = table.api().row($(this).closest('tr')).data();
                var scope = $scope.$new(true);
                scope.device = row.friendly_name;

                $uibModal.open(Object.assign({ scope: scope }, setDeviceStateModal));
                $scope.$apply();
            });


            table.api().rows
                .add($ctrl.devices)
                .draw();
        };

        $ctrl.$onChanges = function(changes) {
            if (!table) {
                return;
            }

            if (changes.devices) {
                table.api().clear();
                table.api().rows
                    .add($ctrl.devices)
                    .draw();
            }
        };

        function dateRenderer(data, type, row) {
            if (type === 'sort' || type === 'type' || !Number.isInteger(data)) {
                return data;
            }

            return DateTime.fromMillis(data).toFormat(dzSettings.serverDateFormat);
        }

        function actionsRenderer(data, type, row) {
            var actions = [];
            actions.push('<button class="btn btn-icon js-set-state" title="' + $.t('Set State') + '"><img src="images/events.png" /></button>');
            actions.push('<button class="btn btn-icon js-rename-device" title="' + $.t('Rename Device') + '"><img src="images/rename.png" /></button>');
            return actions.join('&nbsp;');
        }
    }
});