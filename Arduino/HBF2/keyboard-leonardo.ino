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
