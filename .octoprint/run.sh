# Now using systemd services (see etc/): octoprint webcamd haproxy
# https://community.octoprint.org/t/setting-up-octoprint-on-a-raspberry-pi-running-raspbian-or-raspberry-pi-os/2337#automatic-start-up-3

# This is just for reference for the tried webcam settings.

# old cheap USB-Webcam:
# mjpg_streamer -i 'input_uvc.so -r SXGA' -o 'output_http.so -p 8090' &

# now using Logitech C920 HD Pro:
sudo uvcdynctrl -i /usr/share/uvcdynctrl/data/046d/logitech.xml & # needed to be able to turn off LED
sudo v4l2-ctl --set-ctrl=led1_mode=0 & # turn off blue LEDs around lens that are always on by default
sudo v4l2-ctl --set-ctrl=focus_auto=0 & # https://blog.ktz.me/disable-autofocus-in-octoprint-with-a-logitech-c920-webcam/
sudo v4l2-ctl --set-ctrl=focus_absolute=25 &
# Also fix exposure once in closed box? https://blog.jaimyn.dev/how-to-get-the-best-webcam-quality-with-octoprint/
mjpg_streamer -i 'input_uvc.so -r 1920x1080 -n -l off' -o 'output_http.so -p 8090' & # via `make install`; no more need for prefixing LD_LIBRARY_PATH=/usr/local/lib/mjpg-streamer
# Alternative:
# mv mjpg-streamer/mjpg-streamer-experimental ~/mjpg-streamer
# and edit ~/mjpg-streamer/start.sh

./venv/bin/octoprint serve
