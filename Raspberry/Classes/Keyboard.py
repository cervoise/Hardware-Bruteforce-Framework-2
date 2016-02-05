import os
import time

#Pour du debug, pas besoin d'arduino
class KeyboardTest:
	def __init__(self):
		return None
		
	def press(self, string, delay):
		for letter in string:
			print letter
			time.sleep(delay)
		
	def pressSpecial(self, special):
		print special

#Ajouter une verification que l'arduino est up dans le __init__
class Keyboard:
	def __init__(self):
		self.path = "./main"
		return None
		
	def press(self, string, delay):
		for letter in string:
			os.system(self.path + " " + str(ord(letter)))
			time.sleep(delay)
		
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
