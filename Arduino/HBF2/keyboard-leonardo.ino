#if defined(__AVR_ATmega32U4__)

  #define WHO_AM_I          0xA1 //Leonardo

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
     Keyboard.press(key);
     delay(50);
     Keyboard.releaseAll();
  }
  
  void typeEnter()
  {
     typeKey(KEY_RETURN);
  }

  void typeBackspace()
  {
     typeKey(KEY_BACKSPACE);
  }

  void typeTab()
  {
     typeKey(KEY_TAB);
  }

  void typeEscape()
  {
     typeKey(KEY_ESC);
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
