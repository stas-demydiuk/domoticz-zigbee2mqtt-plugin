define(['app', '../templates/zigbee2mqtt/viz', '../templates/zigbee2mqtt/viz.full.render', '../templates/zigbee2mqtt/leaflet'], function(app, Viz, vizRenderer, leaflet) {
    var viz = new Viz(vizRenderer);

    app.component('zigbee2mqttPlugin', {
        templateUrl: 'app/zigbee2mqtt/index.html',
        controller: Zigbee2MqttPluginController
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

    function Zigbee2MqttPluginController($element, domoticzApi, zigbee2mqtt) {
        var $ctrl = this;

        $ctrl.$onInit = function() {
            $ctrl.devices = [];
            refreshDevices();
        };

        $ctrl.renderNetworkMap = function() {
            return zigbee2mqtt.sendRequest('network_map').then(renderSvg);
        };

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

                    var bounds = [[ 0, 0 ], [ -500, 500 ]];
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

                        $ctrl.renderNetworkMap().then(function() {
                            $ctrl.isMapLoaded = true;
                        })
                    } else {
                        $ctrl.devices = [];
                    }
                });
        }
    }
})