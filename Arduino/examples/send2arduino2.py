#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import time
import argparse

ADDRESS = 0x04

CMD_SEND_STRING = 0x01
CMD_SEND_CHAR = 0x02
CMD_SEND_MOUSE = 0x03
CMD_WHO = 0x04

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVYXYZ0123456789"


# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)


for c in chars:
    print "\t", c, ord(c)
    bus.write_byte_data(ADDRESS, CMD_SEND_STRING, ord(c))
    time.sleep(0.5)

print 'Arduino feedback: ', bus.read_byte(ADDRESS)


#print '\n'

