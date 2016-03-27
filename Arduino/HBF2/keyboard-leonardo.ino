#if defined ARDUINO_AVR_LEONARDO or defined ARDUINO_AVR_MICRO

  #include <Mouse.h>
  #include <KeyboardWithLayouts.h>

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
  
#endif
