#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import sys
import time

class I2C:
	def __init__(self, address):
		self.ADDRESS = address
		
		self.CMD_SEND_STRING = 0x01
		self.CMD_SEND_CHAR = 0x02
		self.CMD_SEND_MOUSE = 0x03
		self.CMD_WHO = 0x04

		self.RESP_WHO = {0x00 : 'Unknown board/Command unknown',
				 0xA1 : 'Arduino Leonardo',
				 #0xB1 : 'Teensy 1.0',
				 #0xB2 : 'Teensy++ 1.0',
				 0xB3 : 'Teensy 2.0',
				 0xB4 : 'Teensy++ 2.0',
				 0xB5 : 'Teensy 3.0',
				 0xB6 : 'Teensy 3.1',
				 0xB7 : 'Teensy LC',
				 0xB8 : 'Teensy 3.2',
		}
		self.response = 0
		# for RPI version 1, use "bus = smbus.SMBus(0)"
		try:
			self.bus = smbus.SMBus(1)
		except:
			print "No I2C install"
			sys.exit(1)
			
	def testConnection(self):
		try:
			self.bus.write_byte_data(self.ADDRESS, self.CMD_WHO, 0)
			self.response = self.bus.read_byte(self.ADDRESS);
		except:
			print "No I2C device found"
			sys.exit(1)
			
		
		if self.RESP_WHO.has_key(self.response):
			return self.response != 0x00
		else:
			return False
			
	def canUnicode(self):
		return self.response >= 0xB5 and self.response <= 0xBF
	
	def sendI2C(self, command, data):
		self.bus.write_i2c_block_data(self.ADDRESS, command, data)
		time.sleep(0.1)
		return self.bus.read_byte(self.ADDRESS)
		
	def sendChar(self, char):
		return self.sendI2C(self.CMD_SEND_STRING, [ord(e) for e in char])
	
	def sendSpecialChar(self, special_char):
		return self.sendI2C(self.CMD_SEND_CHAR, [special_char])
	
	def sendMouse(self, x, y):
		return self.sendI2C(self.CMD_SEND_MOUSE, [x, y])
	
		
		
			
