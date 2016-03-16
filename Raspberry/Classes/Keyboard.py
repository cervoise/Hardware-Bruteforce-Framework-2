import os
import sys
import time
import re

#For test and debug
class KeyboardTest:
	def __init__(self):
		return None
		
	def press(self, string, delay):
		for letter in string:
			print letter
			time.sleep(delay/1000)
		
	def pressSpecial(self, special):
		print special

class MouseAndKeyboard():
	def __init__(self):
		import I2C
		#Adjust in order to made address change easier !!!
		self.i2cConnection = I2C.I2C(0x04)
		#Check if there is an Arduino
		if self.i2cConnection.testConnection() is False:
			print "Something found on I2C, but no Arduino with the good sketch"
			sys.exit(1)
			
	def press(self, string, delay):
		for letter in string:
			if self.isUnicode(letter) and not self.i2cConnection.canUnicode():
				print "This Arduino cannot handle unicode char"
			else:
				self.i2cConnection.sendChar(letter)
				time.sleep(delay/1000)
		
	def pressSpecial(self, special):
		special_value = 0

		if special == "enter":
			special_value = 13
		elif special == "escape":
			special_value = 27
		elif special == "tabulation":
			special_value = 9
		elif special == "backspace":
			special_value = 8
		elif special == "delete":
			special_value = 127
		elif special[0] == "f":
			if re.match('f\d{1,2}', special): #Check if numeric after the 'f', to ignore keys like Fn
				special_value = 58 - 1 + int(special[1:])
		
		if special_value > 0:
			self.i2cConnection.sendSpecialChar(special_value)
		
	#toimplement
	def isUnicode(self, char):
		return False
