#if defined(__MK20DX128__) or defined(__MK20DX256__) or (defined(__AVR_AT90USB1286__) and not TEENSY_LTE20_BIOS)

  #ifndef USB_HID
    #error 'You must select USB Type: Keyboard+Mouse+Joystick in Tools menu'
    //quotes only to avoid syntax coloration in Arduino IDE
  #endif

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
  

  void mouseMove(int x, int y)
  {
    Mouse.move(x, y);
  }

  void mouseClick(int butt, bool state)
  {
    if(state && !Mouse.isPressed(butt))
    {
      Mouse.press(butt);
    }
    else if(!state && Mouse.isPressed(butt))
    {
      Mouse.release(butt);
    }
  }
  
#endif
