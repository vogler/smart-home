#!/usr/bin/bash

for f in **/run.sh; do
  echo "> $f"
  (cd $(dirname "$f"); ./run.sh)
  echo
done

for f in **/*compose.yml; do
  echo "> $f"
  (cd $(dirname "$f"); docker compose up -d)
  echo
done
