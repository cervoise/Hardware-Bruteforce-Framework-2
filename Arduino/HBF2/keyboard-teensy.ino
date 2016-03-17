#if defined(__MK20DX128__) or defined(__MK20DX256__) or (defined(__AVR_AT90USB1286__) and not TEENSY_LTE20_BIOS)

  /*
   0xB1 : 'Teensy 1.0', 
   0xB2 : 'Teensy++ 1.0',
   0xB3 : 'Teensy 2.0',
   0xB4 : 'Teensy++ 2.0',
   0xB5 : 'Teensy 3.0',
   0xB6 : 'Teensy 3.1',
   0xB7 : 'Teensy LC',
   0xB8 : 'Teensy 3.2',
  */
  #define WHO_AM_I          0xB1
  
  void keyboardStart()
  {
     Keyboard.begin();
  }

  void typeString(char *s)
  {
    Keyboard.print(s);
  }

  void typeKey(int key)
  {
    Keyboard.set_key1(char(key));
    Keyboard.send_now();
    Keyboard.set_key1(0);
    Keyboard.send_now();
  }
  

  void moveMouse(int x, int y)
  {
    Mouse.move(buffer[2], buffer[1]);
  }

  int whoami()
  {
    return WHO_AM_I;
  }
  
#endif
