# PiTheremin
Here's some very basic code to get a theremin like instrument working with a Rasberry Pi and a Lidar sensor. 
Use at your own risk;


//This project is no longer maintained, but shared in hope it may be useful. 

I decided to at least make things easier to get started, I'm working on the setup script now, which should install everything.

### The Pi will not create audio on it's own
### It needs to be used like a midi controller
I think crontab has the startup script, I'm not 100% sure. 

All the code that does anything is in KeithOS. 
You need a rotary dila , a  OLED and a Lidar sensor to get this working

I started working on a Scematic, but didn't finish it:
Schematics/TouchLessMidi.fzz
OLED:

https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/



Lidar :
https://makersportal.com/blog/distance-detection-with-the-tf-luna-lidar-and-raspberry-pi

PS: To get this to work you ether want to turn your Pi into a USB midi device or use my other project to transmit Midi over bluetooth.

https://github.com/Mylab6/PiBluetoothMidSetup


TR Lidar needs to be setup with 

https://makersportal.com/blog/distance-detection-with-the-tf-luna-lidar-and-raspberry-pi
