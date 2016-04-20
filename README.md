# Hardware-Bruteforce-Framework-2

Currently under developpement (but as Apache said: it works!).

Needs: 
- a RaspberryPi or something equivalent supporting Linux and i2c
- an Arduino supporting Keyboard.h and Mouse.h (Arduino Leonardo for example) or a Teensy 2.x/3.x.
- 3 wires in order to connect Pi and Arduino
- Optional: an USB webcam (RaspiCam is too slow)

Targets and wordlists support:
- BIOS only supported on Teensy 2.x
- Unicode only supported on Teensy 3.x

Installation (Pi part):
- Enable i2c:
  - apt-get install i2c-tools libi2c-dev python-smbus
  - sed -i 's/^blacklist i2c-bcm2708$/#&/g' /etc/modprobe.d/raspi-blacklist.conf
  - echo -e "i2c-bcm2708\ni2c-dev" >> /etc/modules
  - echo -e "\n#Enable i2c\ndtparam=i2c1=on\ndtparam=i2c_arm=on" >> /boot/config.txt
- apt-get install imagemagick fswebcam
- optionnal (for WOL): apt-get install scapy
- optionnal (for remote analysis): apt-get install python-pip && pip install pyftpdlib
- reboot
- git clone https://github.com/cervoise/Hardware-Bruteforce-Framework-2.git
- cd Hardware-Bruteforce-Framework-2/Raspberry

Installation (Arduino/Teensy part):
- push the Arduino project from Arduino folder.

Wiring:
- Connect your Raspberry Pi and Teensy/Arduino SDA, SCL, and GND pins together

RPI B & Leonardo:

![](Docs/Scheme/Raspberry-ArduinoTeensy/wiring_RPI-Leonardo_bb_thumb.png)

RPI B+ & Teensy 3.0:

![](Docs/Scheme/Raspberry-ArduinoTeensy/wiring_RPI-Teensy30_thumb.png)

More wiring examples can be found in directory Docs/Scheme/Raspberry-ArduinoTeensy/

