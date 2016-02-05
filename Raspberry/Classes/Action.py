import time
import Keyboard

class Action:
	def __init__(self, path_to_pattern):
		self.keyboard = Keyboard.KeyboardTest()
		#self.keyboard = Keyboard.Keyboard()
		self.loop = 0
		self.use_login = False
		self.check_password = False
		self.bruteforce = False
		self.actions_array = []
		for line in open(path_to_pattern):
			self.actions_array.append(line.rstrip())
			self.use_login = self.use_login or line.rstrip().lower() == "login"
			self.check_password = self.check_password or line.rstrip().lower() == "password"
			if line.rstrip().lower().split(' ')[0] == "bruteforce":
				self.bruteforce = True
				#erreur si pas de taille
				self.bruteforce_size_start = line.rstrip().split(' ')[1].split('-')[0]
				self.bruteforce_size_stop = line.rstrip().split(' ')[1].split('-')[1]
				#simplifier si une seule taille
				#verifier/definir taille max de bruteforce

		if self.check_password and self.bruteforce:
			print "Error, cannot use a password and bruteforce"
	
	def doActions(self, password="", login="", delay=0.1):
		for i in range(0, len(self.actions_array)):
			value = self.actions_array[i].lower()
			if value == 'enter' or value == 'tabulation' or value == 'escape' or value == 'backspace':
				self.keyboard.pressSpecial(value)	
			elif value == 'login':
				self.keyboard.press(login, delay)
			elif value == 'password' or value.split(' ')[0] == 'bruteforce':
				self.keyboard.press(password, delay)
			elif value.split(' ')[0] == 'delay':
				time.sleep(int(value.split(' ')[1])/1000)
			#pour l'instant ne gere pas le login ni les caracteres speciaux dans le nom de 
			elif value == 'screenshot':
				os.system("fswebcam " + password + ".jpg") 
			
	def usePassword(self):
		return self.check_password	

	def useLogin(self):
		return self.check_password	
