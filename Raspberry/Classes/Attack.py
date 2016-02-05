import Action
import Wordlist

class Attack:
	def __init__(self, path_to_pattern, path_to_wait = "", path_to_logins = "", path_to_password = "", attempt=0, delay=0.1):
		self.pattern = Action.Action(path_to_pattern)
		if path_to_wait != "":
			self.wait = Action.Action("wait.txt")
			self.attempt = attempt
		else:
			self.wait = None
		if self.pattern.useLogin():
			self.logins = Wordlist.Wordlist(path_to_logins)
		else:
			self.logins = Wordlist.EmptyWordlist()

		if self.pattern.usePassword():
			self.passwords = Wordlist.Wordlist(path_to_password)
		#else:
		#	self.passwordspasswords = Bruteforce

	def doAttack(self):
		if self.wait is not None:
			self.doAttackWithWait()
		else:
			self.doAttackWithoutWait()

	def doAttackWithoutWait(self):
		while self.logins.hasNext():
			login = self.logins.getNext()
			while self.passwords.hasNext():
				password = self.passwords.getNext()
				print password
				self.pattern.doActions(password, login, 0.1)

	def doAttackWithWait(self):
		trial = 0
		while self.logins.hasNext():
			login = self.logins.getNext()
			while self.passwords.hasNext():
				if trial == self.attempt:
					self.wait.doActions()
					trial = 0
				password = self.passwords.getNext()
				print password
				self.pattern.doActions(password, login, 0.1)
				trial += 1
