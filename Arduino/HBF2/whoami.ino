
#if defined ARDUINO_AVR_LEONARDO
  #define WHO_AM_I          0xA1  //Arduino Leonardo
#elif defined ARDUINO_AVR_MICRO
  #define WHO_AM_I          0xA2  //Arduino Micro
#elif defined __AVR_ATmega32U4__
  #define WHO_AM_I          0xB3  //Teensy 2.0
#elif defined __AVR_AT90USB1286__
  #define WHO_AM_I          0xB4  //Teensy++ 2.0
#elif defined __MK20DX128__
  #define WHO_AM_I          0xB5  //Teensy 3.0
#elif defined __MK20DX256__
  #define WHO_AM_I          0xB6  //Teensy 3.1 / 3.2
#elif defined __MKL26Z64__
  #define WHO_AM_I          0xB7  //Teensy LC
#else
  #define WHO_AM_I          0     // Board not supported
#endif

int whoami()
{
  return WHO_AM_I;
}

