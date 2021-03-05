#!/bin/sh
# footswitch.sh
# navigate to home directory, then to this directory, then execute python script, then back home

#sudo python3 /home/pi/PiMidi/controller.py
cd /
cd  /home/pi/PiMidi/
#cd home/pi/midi_controller
sudo python3 controller.py
#midi_controller.py
cd / 
# /home/pi/PiMidi/startScript.sh
#   >/home/pi/logs/cronlog 2>&1

#chmod u+x SCRIPTNAME