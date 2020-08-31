# microbe_obliterator

This repository contains everything needed to turn your irobot braava jet into a real-life mo robot. 

## Installation 
Download this repository on your raspberry pi in the home directory. 

Then create the file /home/pi/.config/autostart/mo.desktop. 

This file should contain the text: 
```
[Desktop Entry]
Type= Application
Name= PiCube
Exec= /usr/bin/python3 /home/pi/microbe_obliterator/mo.py
```


Make sure that in /boot/config.txt you uncomment hdmi_force_hotplug=1, as without this the raspberry pi won't boot in headless mode for me. 
