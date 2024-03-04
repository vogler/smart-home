
# journalctl -u zigbee2mqtt.service -f  | clog z2m
tail -f /opt/zigbee2mqtt/data/log/current/log.txt | clog z2m
