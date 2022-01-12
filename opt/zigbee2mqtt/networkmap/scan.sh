
# https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html#zigbee2mqtt-bridge-request-networkmap
mosquitto_pub -t zigbee2mqtt/bridge/request/networkmap -m 'graphviz'
mosquitto_sub -t zigbee2mqtt/bridge/response/networkmap -C 1 | jq -r .data.value | tee "$(date '+%F %H.%M.%S').dot"
