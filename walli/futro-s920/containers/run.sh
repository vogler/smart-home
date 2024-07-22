#!/usr/bin/bash

# hidden containers (starting with .) are ignored
for f in **/docker-compose.yml; do
  echo "> $f"
  (cd $(dirname "$f"); docker compose up -d)
  echo
done
