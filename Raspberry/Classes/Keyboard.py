import os
import os.path
import sys
import time

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

#Check if Arduino is up and if i2c... exists in __init__
class Keyboard:
	def __init__(self):
		self.path = "./i2c-com-with-duino"
		if os.path.isfile(self.path) is False:
			print "Program for communication with Arduino is not set"
			sys.exit(1)
		return None
		
	def press(self, string, delay):
		for letter in string:
			os.system(self.path + " " + str(ord(letter)))
			time.sleep(delay/1000)
		
	def pressSpecial(self, special):
		if special == "enter":
			special_value = str(13)
		elif special == "escape":
			special_value = str(27)
		elif special == "tabulation":
			special_value = str(9)
		elif special == "backspace":
			special_value = str(8)
		
		os.system(self.path + " " + special_value)