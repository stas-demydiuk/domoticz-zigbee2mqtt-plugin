define([
    'app',
    '../templates/zigbee2mqtt/viz',
    '../templates/zigbee2mqtt/viz.full.render',
    '../templates/zigbee2mqtt/leaflet',
    '../templates/zigbee2mqtt/zigbee_devices',
    '../templates/zigbee2mqtt/zigbee_groups',
    'app/devices/Devices.js'
],
function(app, Viz, vizRenderer, leaflet) {
    var viz = new Viz(vizRenderer);

    app.component('zigbee2mqttPlugin', {
        templateUrl: 'app/zigbee2mqtt/index.html',
        controller: Zigbee2MqttPluginController
    });

    // Allows to load Devices.html which contains templates for <devices-table /> component
    app.component('zigbee2mqttFakeDevices', {
        templateUrl: 'app/devices/Devices.html',
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

            domoticzApi.sendCommand('clearlightlog', {
                idx: idx
            }).catch(function() {
                console.log('Unable to clear log for device idx:' + idx)
            });
        }

        function sendRequest(command, params) {
            var deferred = $q.defer();
            var requestId = ++requestsCount;

            var requestInfo = {
                requestId: requestId,
                deferred: deferred,
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
            }).catch(function(error) {
                deferred.reject(error);
            });

            return deferred.promise;
        }

        function handleResponse(data) {
            if (data.type !== 'response' && data.type !== 'status') {
                return;
            }

            var requestIndex = requestsQueue.findIndex(function(item) {
                return item.requestId === data.requestId;
            });

            if (requestIndex === -1) {
                return;
            }

            var requestInfo = requestsQueue[requestIndex];

            if (data.type === 'status') {
                requestInfo.deferred.notify(data.payload);
                return;
            }

            if (data.isError) {
                requestInfo.deferred.reject(data.payload);
            } else {
                requestInfo.deferred.resolve(data.payload);
            }

            requestsQueue.splice(requestIndex, 1);
        }
    });

    function Zigbee2MqttPluginController($element, $scope, Device, domoticzApi, dzNotification, zigbee2mqtt) {
        var $ctrl = this;

        $ctrl.selectPlugin = selectPlugin;
        $ctrl.getVersionString = getVersionString;
        $ctrl.renderNetworkMap = renderNetworkMap;
        $ctrl.fetchZigbeeDevices = fetchZigbeeDevices;
        $ctrl.fetchZigbeeGroups = fetchZigbeeGroups;
        $ctrl.togglePermitJoin = togglePermitJoin;
        $ctrl.refreshDomoticzDevices = refreshDomoticzDevices;

        $ctrl.$onInit = function() {
            $ctrl.selectedApiDeviceIdx = null;
            $ctrl.devices = [];

            refreshDomoticzDevices().then(function() {
                $ctrl.pluginApiDevices = $ctrl.devices.filter(function(device) {
                    return device.Unit === 255
                });

                if ($ctrl.pluginApiDevices.length > 0) {
                    $ctrl.selectPlugin($ctrl.pluginApiDevices[0].idx);
                }
            });

            $scope.$on('device_update', function(event, deviceData) {
                var device = $ctrl.devices.find(function(device) {
                    return device.idx === deviceData.idx && device.Type === deviceData.Type;
                });

                if (device) {
                    Object.assign(device, deviceData);
                }
            });
        };

        function selectPlugin(apiDeviceIdx) {
            $ctrl.selectedApiDeviceIdx = apiDeviceIdx;
            zigbee2mqtt.setControlDeviceIdx(apiDeviceIdx);

            $ctrl.controllerInfo = null;
            $ctrl.zigbeeDevices = null;
            $ctrl.zigbeeGroups = null;
            $ctrl.isMapLoaded = false;

            fetchControllerInfo()
                .then(fetchZigbeeDevices)
                .then(fetchZigbeeGroups);
        }

        function fetchZigbeeDevices() {
            return zigbee2mqtt.sendRequest('devices_get').then(function(devices) {
                $ctrl.zigbeeDevices = devices.map(function(device) {
                    return Object.assign({
                        model: null,
                    }, device, {
                        lastSeen: device.lastSeen || 'N/A',
                        description: device.description || '',
                        model: device.model || 'N/A',
                        type: device.type || 'N/A'
                    });
                }).sort(function(a, b) {
                    return a.friendly_name < b.friendly_name ? -1 : 1
                });
            });
        }

        function fetchZigbeeGroups() {
            return zigbee2mqtt.sendRequest('groups_get').then(function(groups) {
                $ctrl.zigbeeGroups = groups
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

        function refreshDomoticzDevices() {
            return domoticzApi.sendRequest({
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
                            })
                            .map(function(device) {
                                return new Device(device)
                            })
                    } else {
                        $ctrl.devices = [];
                    }
                });
        }
    }
});