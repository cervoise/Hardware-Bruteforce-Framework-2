
//Set to true if you intend to use a Teensy(++) 2.0 as a keyboard in a bios
#define TEENSY_LTE20_BIOS true

// Your Arduino/teensy slave i2c address
#define SLAVE_ADDRESS     0x04


#if defined(__AVR_ATmega32U4__)
  #include <Mouse.h>
  #include <KeyboardWithLayouts.h>
#endif

#include <Wire.h>

#define CMD_SEND_STRING   0x01
#define CMD_SEND_CHAR     0x02
#define CMD_SEND_MOUSE    0x03
#define CMD_WHO           0x04

#define BUFFER_LEN        10
int buffer[BUFFER_LEN];

int ack = 0;
 
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
  ack = 0;
  int n = 0;

  while(Wire.available() && n < byteCount) {
    if(n < BUFFER_LEN) {
      buffer[n++] = Wire.read();
    }
    else {
      // Ignore remaining data if BUFFER_LEN has been reached
      Wire.read();
    }
  }

  // First byte received is the command
  switch(buffer[0]) {
    case CMD_WHO:
      ack = whoami();
      break;
    
    case CMD_SEND_STRING:
      char string[BUFFER_LEN];
      for(int i = 1 ; i < n ; i++) {
        string[i-1] = char(buffer[i]);
      }
      string[n-1] = '\0';
      typeString(string); 
      ack = 1;
      break;
    
    case CMD_SEND_CHAR:
      type_char(buffer[1]);
      ack = 1;
      break;
    
    case CMD_SEND_MOUSE:
      moveMouse(buffer[2], buffer[1]);
      ack = 1;
      break;
  }

}

void type_char(int number) {
  switch (number) {
    case 8:   //BS
    case 127: //DEL
      typeBackspace();
      break;
    case 9:
      typeTab();
      break;
    case 10:  //LF
    case 13:  //CR
      typeEnter();
      break;
    case 27:
      typeEscape();
      break;
    default:
      typeKey(number);
  }
}

// callback for sending data
void sendData() {
  Wire.write(ack);
}
