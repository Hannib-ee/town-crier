#!/bin/bash

#Random line
ENCOUNTER=$(grep . /home/hannibee/Documents/Projects/DnD/encounters.txt | shuf -n 1)

#Get date
DATE=$(date)

#Display message
echo "--- TOWN CRIER REPORT: $DATE ---" >> /home/hannibee/Documents/Projects/DnD/chronicles.txt
echo "Today's Event: $ENCOUNTER" >> /home/hannibee/Documents/Projects/DnD/chronicles.txt
echo "--------------------------------" >> /home/hannibee/Documents/Projects/DnD/chronicles.txt

