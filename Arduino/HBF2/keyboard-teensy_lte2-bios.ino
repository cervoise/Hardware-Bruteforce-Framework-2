#if defined(__AVR_AT90USB1286__) and TEENSY_LTE20_BIOS

  // USB Type must be defined to "Serial" in order to use this code

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
  #define WHO_AM_I          0xB4
  
  #include <avr/io.h>
  #include <avr/pgmspace.h>
  #include <avr/interrupt.h>
  #include <util/delay.h>
  #include <usb_keyboard.h>
  
  
  #define NULL_MODIFIER     0
  
  void keyboardStart() 
  {
     usb_init();
     while (!usb_configured()) /* wait */ ;
  }

  void typeString(char *s)
  {
    //Keyboard.print(s);
  }

  void typeKey(int key)
  {
    /*
    Keyboard.set_key1(char(key));
    Keyboard.send_now();
    Keyboard.set_key1(0);
    Keyboard.send_now();
    */
  }
  
  void typeEnter()
  {
    usb_keyboard_press(KEY_ENTER, NULL_MODIFIER);
  }

  void typeBackspace()
  {
     usb_keyboard_press(KEY_BACKSPACE, NULL_MODIFIER);
  }

  void typeTab()
  {
     usb_keyboard_press(KEY_TAB, NULL_MODIFIER);
  }

  void typeEscape()
  {
     usb_keyboard_press(KEY_ESC, NULL_MODIFIER);
  }

  void moveMouse(int x, int y)
  {
    //Can't move mouse here. Set TEENSY_LTE20_BIOS to false to use mouse.
  }

  int whoami()
  {
    return WHO_AM_I;
  }
  
#endif
