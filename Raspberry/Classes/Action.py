import os.path
import sys
import time

import IoTPlug
import Keyboard
import WOL

class Action:
	def __init__(self, path_to_pattern, path_to_screenshots='', no_screenshots=False, DEBUG=False):
		
		if DEBUG:
			self.keyboard = Keyboard.KeyboardTest()
		else:
			self.keyboard = Keyboard.MouseAndKeyboard()
		
		self.use_login = False
		self.last_login = ''
		self.new_login_delay = 0
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
				lineCleaned = line.rstrip().lower()
				
				#Add the line to the array (don't add the screenshot command if no_screenshots is true)
				if not (lineCleaned == "screenshot" and no_screenshots):
					self.actions_array.append(lineCleaned)
				
				#import WOL if needed
				if lineCleaned.split(' ')[0] == 'wol':
					import WOL
	
				#Var in order to check if pattern is good with command line
				self.use_login = self.use_login or lineCleaned == "login" or lineCleaned.split(' ')[0] == "login"
				self.check_password = self.check_password or lineCleaned == "password"
				self.use_screenshot = self.use_screenshot or lineCleaned == "screenshot"
				
				#Check for login delay
				if lineCleaned.split(' ')[0] == "login" and len(lineCleaned.split(' ')) == 2:
					self.new_login_delay = lineCleaned.split(' ')[1]
					
				#Check for delaypassword
				if lineCleaned.split(' ')[0] == "delaypassword":
					self.delay = int(lineCleaned.split(' ')[1])
				
				#Check for wait
				if lineCleaned.split(' ')[0] == "wait":
					if len(line.rstrip().split(' ')) != 3:
						print "Wait instruction is not correct: wait file attempt"
						sys.exit(1)
					if path_to_pattern.rpartition('/')[0] != '':
						wait_file = path_to_pattern.rpartition('/')[0] + '/' + line.rstrip().split(' ')[1]
					else:
						wait_file = line.rstrip().split(' ')[1]
					if os.path.isfile(wait_file) is False:
						print "Wait function in " + path_to_pattern + " is not correct"
						sys.exit(1)
					self.wait = Action(wait_file, path_to_screenshots, no_screenshots, DEBUG)
					self.attempt = int(lineCleaned.split(' ')[2])
						
				#Check for bruteforce
				if lineCleaned.split(' ')[0] == "bruteforce":
					self.bruteforce = True
					#add error if no size
					#key: bruteforce charset (numeric, alphaLower, alphaUpper, alpha, alphaNumericLower,  alphaNumericUpper, alphaNumeric) sizemin-sizemax
					#one size possible
					line_split = lineCleaned.split(' ')
					self.bruteforce_charset = line_split[1].lower()
					if len(line_split[2].split('-')) == 2:
						self.bruteforce_size_start = int(line_split[2].split('-')[0])
						self.bruteforce_size_stop = int(line_split[2].split('-')[1])
					else:
						self.bruteforce_size_start = int(line_split[2])
						self.bruteforce_size_stop = int(line_split[2])
					if self.bruteforce_size_stop > 6:
						print "Error, bruteforce size is too high"
						sys.exit(1)
		print self.actions_array

		if no_screenshots is True:
			self.use_screenshot = False
		
		#Check if pattern is good with command line
		if self.check_password and self.bruteforce:
			print "Error, cannot use a password and bruteforce"
			sys.exit(1)		
	
	def doActions(self, password="", login="", trial=0):
		for i in range(0, len(self.actions_array)):
			value = self.actions_array[i]
			valueSplit = value.split(' ')
			
			if value in ['enter', 'tabulation', 'escape', 'backspace', 'delete', 'left', 'right', 'up', 'down'] or (value[0] == 'f' and len(value)<4):
				self.keyboard.pressSpecial(value)	
			elif valueSplit[0] == 'flood':
				#flood KEY time [sleep]
				key = valueSplit[1]
				timeout = time.time() + (int(valueSplit[2]) / 1000.)
				sleep = 0 if len(valueSplit) < 4 else int(valueSplit[3])/1000.
				while time.time() < timeout:
					self.keyboard.pressSpecial(key)
					time.sleep(sleep)
			elif valueSplit[0] == 'spam':
				raise ValueError('"spam" command has been replaced by "flood"')
			elif value == 'login' or valueSplit[0] == 'login':
				self.keyboard.press(login, self.delay)
			elif value == 'password' or valueSplit[0] == 'bruteforce':
				self.keyboard.press(password, self.delay)
			elif valueSplit[0] == 'delay':
				time.sleep(int(valueSplit[1])/1000.)
			elif value == 'screenshot':
				command_line = "fswebcam --no-banner "
				if self.screenshots != '':
					command_line += self.screenshots + "/"
				if self.useLogin():
					if os.path.isdir(self.screenshots + "/" + login) is False:
						os.system("mkdir -p " + self.screenshots + "/" + login)
					command_line += login + "/"
				command_line += self.checkFileForPicture(password) + ".jpg"
				print command_line
				os.system(command_line) 
			elif valueSplit[0] == 'wait':
				if trial % self.attempt == 0:
					self.wait.doActions()
			elif valueSplit[0] == 'wol':
				WOL.WOL(valueSplit[1])
			elif valueSplit[0] == 'wemo':
				ip = valueSplit[1]
				status = valueSplit[2].upper()
				if status == 'ON':
					IoTPlug.on(ip)
				else:
					IoTPlug.off(ip)
			elif valueSplit[0] == 'gpio':
				pin = int(valueSplit[1])
				sleep = int(valueSplit[2])/1000.
				path = os.path.dirname(os.path.realpath(__file__)) + "/scripts"
				os.system("sudo python %s/gpio.py %d %f" % (path, pin, sleep))

		#If login changed since last try, we add a delay

	def checkFileForPicture(self, filename):
		if os.path.isfile(self.cleanPasswordForFileName(filename)):
			return self.checkFileForPicture(filename + "--0")
		return self.cleanPasswordForFileName(filename)
	
	def cleanPasswordForFileName(self, password):
		return password.replace('/', '-')
		
	def useWait(self):
		return self.wait
		
	def usePassword(self):
		return self.check_password	
	
	def useBruteforce(self):
		return self.bruteforce
	
	def getBruteforceCharset(self):
		return self.bruteforce_charset
	
	def getBruteforceSizeMin(self):
		return self.bruteforce_size_start 
	
	def getBruteforceSizeMax(self):
		return self.bruteforce_size_stop
	
	def useLogin(self):
		return self.use_login
	
	def useScreenshot(self):
		return self.use_screenshot
