#if defined(__MK20DX128__) or defined(__MK20DX256__) or (defined(__AVR_AT90USB1286__) and not TEENSY_LTE20_BIOS)

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
  
#endif
