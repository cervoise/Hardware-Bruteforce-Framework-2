# Hardware-Bruteforce-Framework-2

Actually under developpement.

Needs: 
- a RaspberryPi or something equivalent supporting Linux and i2c
- an Arduino supporting Keyboard.h and Mouse.h (Arduino Leonardo for example) or a Teensy 3.x.
- 3 cables in order to connect Pi and Arduino
- Optionnal: an USB webcam (RaspiCam is to slow)

Installation (Pi part):
- configure i2c using raspi-config
- apt-get install imagemagick fswebcam i2c-tools
- reboot
- git clone https://github.com/cervoise/Hardware-Bruteforce-Framework-2.git
- cd Hardware-Bruteforce-Framework-2/Raspberry
- gcc i2c-com-with-duino.c -o i2c-com-with-duino

Installation (Arduino/Teensy part):
- push the Arduino project from Arduino folder.
