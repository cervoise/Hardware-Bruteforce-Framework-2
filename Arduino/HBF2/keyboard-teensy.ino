#if defined(__MK20DX128__) or defined(__MK20DX256__)
//Pas encore utilisable, s'assurer que l'on peut entrer un entier pour tapper une lettre

  void keyboardStart()
  {
     Keyboard.begin();
  }

  void typeKey(int key)
  {
    Keyboard.set_key1(key);
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
#endif
