# ~/.node-red/flows_rpi3.json is compact in one line
# Before I exported all flows as formatted JSON from the web UI and pasted them.
# This script instead just pretty-prints the current config and overwrites the config in the repo.
# https://stackoverflow.com/questions/352098/how-can-i-pretty-print-json-in-a-shell-script
# `jq .` and `python -m json.tool` reordered/sorted fields; with `python3 -m json.tool` it's stable.
cat ~/.node-red/flows_rpi3.json | python3 -m json.tool > ~/smart-home/.node-red/flows_rpi3.json
