# See ~/smart-home/.node-red/export_flows.sh for details
cat ~/.node-red/flows.json | python3 -m json.tool > ~/smart-home/walli/.node-red/flows.json
