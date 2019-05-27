![Chronograf dashboard](https://i.imgur.com/KdjZi8j.png)
![node-red light automation](https://i.imgur.com/qlGAEON.png)

- Raspberry Pi 3 B
  - First used [home-assistant](https://www.home-assistant.io/), now only [node-red](https://nodered.org/).
    - home-assistant was slow, didn't use UI anyway; node-red is much nicer for automation and for playing around.
  - [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt/) ([config](opt/zigbee2mqtt/data/configuration.yaml))
    - Aqara door sensors, Hue motion sensors, Hue and Ikea Tradfri lights
    - First used CC2531 USB stick, now CC2530 via UART USB because of supposed better range.
  - [Sensors](https://github.com/vogler/sensors) -> [MQTT](https://mosquitto.org/) -> [Telegraf](https://github.com/influxdata/telegraf) -> [InfluxDB](https://github.com/influxdata/influxdb) -> [Chronograf](https://github.com/influxdata/chronograf)
- Wemos D1 mini: [FlowMeter](https://github.com/vogler/FlowMeter) for shower usage
