![Chronograf dashboard](https://i.imgur.com/KdjZi8j.png)
![node-red light automation](https://i.imgur.com/qlGAEON.png)

Devices:
- Raspberry Pi 3 & 4:
  - First used [home-assistant](https://www.home-assistant.io/), now only [node-red](https://nodered.org/).
    - home-assistant was slow, didn't use UI anyway; node-red is much nicer for automation and for playing around.
  - [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt/) ([config](opt/zigbee2mqtt/data/configuration.yaml))
    - Aqara door sensors, Hue motion sensors, Hue and Ikea Tradfri lights
    - First used CC2531 USB stick, now CC2530 via UART USB because of supposed better range.
  - [Sensors](https://github.com/vogler/sensors) -> [MQTT](https://mosquitto.org/) -> [Telegraf](https://github.com/influxdata/telegraf) (collects metrics) -> [InfluxDB](https://github.com/influxdata/influxdb) (TSDB) -> [Chronograf](https://github.com/influxdata/chronograf) (web GUI, graphs)
    - InfluxDB is not reliable on 32 bit OS, fails to allocate memory and somehow crashes the RPi every couple of days (see [issue](https://github.com/influxdata/influxdb/issues/11339#issuecomment-525500034)), partially fixed by switching to 64 bit kernel on RPi4, see [influxdb-fail.md](influxdb-fail.md).
- Wemos D1 mini: [FlowMeter](https://github.com/vogler/FlowMeter) for shower usage
- Wemos D1 mini: 16x16 WS2812B LED matrix with [WLED](https://github.com/Aircoookie/WLED) and custom [wled.py](https://github.com/vogler/smart-home/blob/master/wled.py) to show CO2 level and other numbers. In 3D-printed case with black PLA grid to separate pixels, sandwich paper as diffusor and dark acrylic glass plate as screen cover.
- Artillery Genius 3D printer, see [gist](https://gist.github.com/vogler/588c577a37f5a573afa5b1000307d41b) for modifications & config
- switches/sockets:
  - Flashed with [Tasmota](https://github.com/arendst/Tasmota):
    - Sonoff-Touch-Bad: wall switch for bathroom
    - Sonoff-S20-LED-Strip: ~4m of 5m 5054 120LEDs/m Cool White 12V on 10A power supply, installed in angled alu mount with white diffusor
    - Sonoff-S26-Genius: 3D printer & E27 LED bulb in Ikea Lack table enclosure
  - BlitzWolf-BW-SHP6-TV: has power measurement
- Roborock-S50 vacuum robot
- SmartMi-Fan-2S
- Amazon-Echo-Dot

### external access
#### IPv6 from IPv4
[M-net](https://www.m-net.de/hilfe-service/fragen-und-antworten/frage/show/kann-ich-mit-ipv6-auch-auf-netzwerk-ressourcen-mit-ipv4-adresse-weiterhin-zugreifen/1/internetanschluss/) is using [Dual-Stack Lite](https://en.wikipedia.org/wiki/IPv6_transition_mechanism#Dual-Stack_Lite_(DS-Lite)) ([de](https://www.elektronik-kompendium.de/sites/net/2010211.htm)) which means I only have a public IPv6 address and carrier-grade NAT for IPv4.
Only had IPv4 on the phone with o2, but since [june 2021](https://www.teltarif.de/o2-ipv6-mobilfunknetz/news/84237.html) they also support IPv6.
Still, when traveling, mobile/hotel WiFi might have IPv4 only. Check with https://ipv6-test.com.

Free solutions for accessing IPv6 from IPv4-only connections:
- [localtunnel](https://github.com/localtunnel/localtunnel) for each port: `npx localtunnel --port 8080`
- [tailscale](https://tailscale.com): Point-to-point WireGuard VPN
- [6to4 relay](https://en.wikipedia.org/wiki/6to4): have not tried

#### DNS
Using [MyFRITZ](https://www.myfritz.net/) DynDNS in FritzBox, rpi{3,4}.voglerr.de subdomains with cloudflare as nameserver for proxy/stats and [CNAME flattening](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/) which allows CNAME for domain root as well.

#### VPN
Using [PiVPN](https://www.pivpn.io/) for WireGuard with clients on MBA and phone.
Unfortunately can't access the VPN IPs if the foreign network happens to use the same subnet (all FritzBox seem to use 192.168.178.1 - could change mine to e.g. 192.168.0.1, but that's not a failsafe solution).
