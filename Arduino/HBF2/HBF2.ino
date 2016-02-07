#if defined(__AVR_ATmega32U4__)
  #include <Mouse.h>
  #include <Keyboard.h>
#endif

#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int number = 0;
 
void setup() {

 //Starting keyboard
 keyboardStart();

 // initialize i2c as slave
 Wire.begin(SLAVE_ADDRESS);
 
 // define callbacks for i2c communication
 Wire.onReceive(receiveData);
 Wire.onRequest(sendData);
}
 
void loop() {
 delay(100);
}
 
// callback for received data
void receiveData(int byteCount){
 
 while(Wire.available()) {
  number = Wire.read();
  if (number > 31) {
    typeKey(number);
  }
  else {
    switch (number) {
      case 8:
        typeBackspace();
        break;
      case 9:
        typeTab();
        break;
      case 13:
        typeEnter();
        break;
      case 27:
        typeEscape();
        break;
    }
  }
 }
}
 
// callback for sending data
void sendData(){
 Wire.write(number);
}
