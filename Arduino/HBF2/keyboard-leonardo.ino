#if defined(__AVR_ATmega32U4__)

  #define WHO_AM_I          0xA1 //Leonardo

  void keyboardStart()
  {
     Keyboard.begin();
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

  int whoami()
  {
    return WHO_AM_I;
  }
  
#endif
