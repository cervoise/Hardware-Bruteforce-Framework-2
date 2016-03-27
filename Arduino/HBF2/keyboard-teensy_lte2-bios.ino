#if defined(__AVR_AT90USB1286__) and TEENSY_LTE20_BIOS

  // USB Type must be defined to "Serial" in order to use this code
  
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
    usb_keyboard_print(s[0]);
  }

  void typeKey(int key)
  {
    usb_keyboard_press(key, NULL_MODIFIER);
  }
  
  void moveMouse(int x, int y)
  {
    //Can't move mouse here. Set TEENSY_LTE20_BIOS to false to use mouse.
  }
  
#endif
