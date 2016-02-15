#if defined(__MK20DX128__) or defined(__MK20DX256__)
//Pas encore utilisable, s'assurer que l'on peut entrer un entier pour tapper une lettre

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
  #define WHO_AM_I          0xB5
  
  void keyboardStart()
  {
     Keyboard.begin();
  }

  void typeKey(int key)
  {
    Keyboard.set_key1(char(key));
    Keyboard.send_now();
    Keyboard.set_key1(0);
    Keyboard.send_now();
  }
  
  void typeEnter()
  {
     typeKey(KEY_ENTER);
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
