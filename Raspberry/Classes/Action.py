import os.path
import sys
import time

import Keyboard

#completer fonction de nettoyage nom de repertoire

class Action:
	def __init__(self, path_to_pattern, path_to_screenshots='', no_screenshots=False):
		#self.keyboard = Keyboard.KeyboardTest()
		self.keyboard = Keyboard.Keyboard()
		#self.loop = 0
		
		self.use_login = False
		self.check_password = False
		self.use_screenshot = False
		
		self.bruteforce = False
		
		self.actions_array = []
		
		self.delay = 100
		self.wait = None
		
		if path_to_screenshots != '' and os.path.isdir(path_to_screenshots) is False:
			os.system("mkdir -p " + path_to_screenshots)
		self.screenshots = path_to_screenshots
		for line in open(path_to_pattern):
			if line[0] != '#':
				#Add the line to the array
				if line.rstrip().lower() == "screenshot":
					if no_screenshots is False:
						self.actions_array.append(line.rstrip())
				else:
					self.actions_array.append(line.rstrip())
					
				#Var in order to check if pattern is good with command line
				self.use_login = self.use_login or line.rstrip().lower() == "login"
				self.check_password = self.check_password or line.rstrip().lower() == "password"
				self.use_screenshot = self.check_password or line.rstrip().lower() == "screenshot"
		
				#If specific attribution in pattern file
				if line.rstrip().lower().split(' ')[0] == "delaypassword":
					self.delay = int(line.rstrip().lower().split(' ')[1])
					#print self.delay
				if line.rstrip().lower().split(' ')[0] == "wait":
					try:
						if path_to_pattern.rpartition('/')[0] != '':
							wait_file = path_to_pattern.rpartition('/')[0] + '/' + line.rstrip().split(' ')[1]
						else:
							wait_file = line.rstrip().split(' ')[1]
						self.wait = Action(wait_file)
						self.attempt = int(line.rstrip().lower().split(' ')[2])
					except:
						print "Wait function in " + path_to_pattern + " is not correct"
						sys.exit(1)
				if line.rstrip().lower().split(' ')[0] == "bruteforce":
					self.bruteforce = True
					#erreur si pas de taille
					self.bruteforce_size_start = line.rstrip().split(' ')[1].split('-')[0]
					self.bruteforce_size_stop = line.rstrip().split(' ')[1].split('-')[1]
					#simplifier si une seule taille
					#verifier/definir taille max de bruteforce
		
		if no_screenshots is True:
			self.use_screenshot = False
		
		#Check if pattern is good with command line
		
		if self.check_password and self.bruteforce:
			print "Error, cannot use a password and bruteforce"
			sys.exit(1)
		
		
			
	
	def doActions(self, password="", login="", trial=0):
		for i in range(0, len(self.actions_array)):
			value = self.actions_array[i].lower()
			if value == 'enter' or value == 'tabulation' or value == 'escape' or value == 'backspace':
				self.keyboard.pressSpecial(value)	
			elif value == 'login':
				self.keyboard.press(login, self.delay)
			elif value == 'password' or value.split(' ')[0] == 'bruteforce':
				self.keyboard.press(password, self.delay)
			elif value.split(' ')[0] == 'delay':
				time.sleep(int(value.split(' ')[1])/1000)
			elif value == 'screenshot':
				command_line = "fswebcam --no-banner "
				if self.screenshots != '':
					command_line += self.screenshots + "/"
				if self.useLogin():
					if os.path.isdir(self.screenshots + "/" + login) is False:
						os.system("mkdir -p " + self.screenshots + "/" + login)
					command_line += login + "/"
				command_line += self.cleanPasswordForFileName(password) + ".jpg"
				print command_line
				os.system(command_line) 
			elif value.split(' ')[0] == 'wait':
				if trial % self.attempt == 0:
					self.wait.doActions()
	
	def cleanPasswordForFileName(self, password):
		return password
		
	def useWait(self):
		return self.wait
		
	def usePassword(self):
		return self.check_password	

	def useLogin(self):
		return self.use_login
	
	def useScreenshot(self):
		return self.use_screenshot
