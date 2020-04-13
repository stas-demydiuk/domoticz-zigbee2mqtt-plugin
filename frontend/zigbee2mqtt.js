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

    function Zigbee2MqttPluginController($scope, $element, domoticzApi, zigbee2mqtt) {
        var $ctrl = this;

        $ctrl.renderNetworkMap = renderNetworkMap;
        $ctrl.fetchZigbeeDevices = fetchZigbeeDevices;

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

        function renderNetworkMap() {
            if ($ctrl.isMapLoaded) {
                return;
            }

            zigbee2mqtt.sendRequest('network_map').then(renderSvg).then(function() {
                $ctrl.isMapLoaded = true;
            });
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
                        fetchZigbeeDevices()
                    } else {
                        $ctrl.devices = [];
                    }
                });
        }
    }

    function Zigbee2MqttDevicesTableController($element, dzSettings, dataTableDefaultSettings) {
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
                ],
            }));

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
    }
});