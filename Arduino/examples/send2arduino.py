#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import time
import argparse

ADDRESS = 0x04

CMD_SEND_STRING = 0x01
CMD_SEND_CHAR = 0x02
CMD_MOUSE_MOVE = 0x03
CMD_MOUSE_CLICK = 0x06
CMD_WHO = 0x04
CMD_PRESS_MULTIPLE = 0x05

RESP_WHO = {0x00 : 'Unknown board/Command unknown',
            0xA1 : 'Arduino Leonardo',
            0xA2 : 'Arduino Micro',
            0xB3 : 'Teensy 2.0',
            0xB4 : 'Teensy++ 2.0',
            0xB5 : 'Teensy 3.0',
            0xB6 : 'Teensy 3.1 / 3.2',
            0xB7 : 'Teensy LC',
}

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)


parser = argparse.ArgumentParser(description='Test i2c messages')
parser.add_argument('-w', help='sends command "Who are you?"', action='store_true')
parser.add_argument('-p', help='send P (=number of) multiple chars or keys', type=int)
parser.add_argument('-s', help='send a character', type=str)
parser.add_argument('-c', help='send a special key code', type=int)
parser.add_argument('-m', help='move mouse X Y', nargs=2, type=int, metavar=("X", "Y"))
parser.add_argument('-k', help='click mouse button : BUTTON(left:0/right:1/middle:2) STATE(0/1)', nargs=2, type=int, metavar=("BUTTON", "STATE"))

args = parser.parse_args()
#print (args)

if args.w:
    print '- Who are you?'
    bus.write_byte_data(ADDRESS, CMD_WHO, 0)
    r = bus.read_byte(ADDRESS);
    if RESP_WHO.has_key(r):
        print '- I am a', RESP_WHO[r]
    else:
        print 'Unknown response code:', r

if args.p:
    bus.write_byte_data	(ADDRESS, CMD_PRESS_MULTIPLE, args.p)
elif args.s:
    bus.write_i2c_block_data(ADDRESS, CMD_SEND_STRING, [ord(e) for e in args.s])
elif args.c:
    bus.write_byte_data(ADDRESS, CMD_SEND_CHAR, args.c)
elif args.m:
    bus.write_i2c_block_data(ADDRESS, CMD_MOUSE_MOVE, args.m)
elif args.k:
    bus.write_i2c_block_data(ADDRESS, CMD_MOUSE_CLICK, args.k)
else:
    if not args.w:
        print "Nothing sent to arduino."
    raise SystemExit

print 'Arduino feedback: ', bus.read_byte(ADDRESS)


#print '\n'

