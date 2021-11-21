# list install commands for plugins in config
import yaml
from os.path import expanduser
ids = []
with open(expanduser('~/.octoprint/config.yaml'), "r") as stream:
    config = yaml.safe_load(stream)
    ids = config['plugins'].keys()

import urllib.request, json 
with urllib.request.urlopen("https://plugins.octoprint.org/plugins.json") as url:
    plugins = json.loads(url.read().decode())
    for plugin in plugins:
        if plugin['id'] in ids:
            print('pip install', plugin['archive'])
