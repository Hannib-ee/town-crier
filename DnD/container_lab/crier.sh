#!/bin/bash
while true; do
  ENCOUNTER=$(grep . /usr/local/bin/encounters.txt | shuf -n 1)
  DATE=$(date)
  
  echo "--- TOWN CRIER REPORT: $DATE ---"
  echo "Today's Event: $ENCOUNTER"
  echo "--------------------------------"
  
  sleep 3600
done
