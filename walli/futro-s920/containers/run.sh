#!/usr/bin/bash

for f in **/docker-compose.yml; do
  echo "> $f"
  (cd $(dirname "$f"); docker compose up -d)
  echo
done
