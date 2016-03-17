#if defined(__AVR_ATmega32U4__)

  #include <Mouse.h>
  #include <KeyboardWithLayouts.h>

  #define WHO_AM_I          0xA1 //Leonardo

  #define KEYBOARD_FRENCH
//  #define KEYBOARD_ENGLISH

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
  
  void moveMouse(int x, int y)
  {
    Mouse.move(buffer[2], buffer[1]);
  }

  int whoami()
  {
    return WHO_AM_I;
  }
  
#endif
