Checks which devices are connected to my FritzBox.
See https://fritzconnection.readthedocs.io/en/1.8.0/sources/library.html#fritzhosts.

First install [poetry](https://github.com/python-poetry/poetry), then
~~~console
$ poetry install
# lists all devices
$ poetry run fritzhosts -p <password>
# lists active devices (supply fritz_pwd in config.py)
$ poetry run python active-hosts.py
# True/False (supply phone_mac in config.py)
$ poetry run python phone-connected.py
~~~

## Presence detection via phone, MQTT:
- https://tasker.joaoapps.com/userguide/en/loctears.html
- https://community.home-assistant.io/t/presence-detection-via-tasker-and-mqtt-android-only/21643
- https://www.reddit.com/r/tasker/comments/a6q8vl/looking_for_better_mqtt_integration/
