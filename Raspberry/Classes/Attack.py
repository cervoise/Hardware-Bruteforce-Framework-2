import sys

import Action
import Wordlist

class Attack:
	def __init__(self, path_to_pattern, path_to_logins = "", path_to_passwords = "", path_to_screenshots = "", no_screenshots=False):
		self.pattern = Action.Action(path_to_pattern, path_to_screenshots, no_screenshots)
		
		#Check if pattern is good with command line
		if path_to_screenshots != '' and self.pattern.useScreenshot() is False:
			print "A screenshots folder is specified, but there is not screenshot command in pattern file."
			sys.exit(1)
		if path_to_logins != '' and self.pattern.useLogin() is False:
			print "A logins file is specified, but there is not login command in pattern file."
			sys.exit(1)
		elif path_to_logins == '' and self.pattern.useLogin() is True:
			print "A login command is in pattern file, but there is not logins file specified."
			sys.exit(1)
			
		if path_to_passwords != '' and self.pattern.usePassword() is False:
			print "A passwords file is specified, but there is not password command in pattern file."
			sys.exit(1)
		elif path_to_passwords == '' and self.pattern.usePassword() is True:
			print "A password command is in pattern file, but there is not passwords file specified."
			sys.exit(1)
		
		if self.pattern.useLogin():
			self.logins = Wordlist.Wordlist(path_to_logins)
		else:
			self.logins = Wordlist.EmptyWordlist()

		if self.pattern.usePassword():
			self.passwords = Wordlist.Wordlist(path_to_passwords)
		elif self.pattern.useBruteforce():
			self.passwords = Wordlist.BruteforceMultipleSize(self.pattern.getBruteforceCharset(), self.pattern.getBruteforceSizeMin(), self.pattern.getBruteforceSizeMax())
			
	def doAttack(self):
		if self.pattern.useWait() is not None:
			self.doAttackWithWait()
		else:
			self.doAttackWithoutWait()

	def doAttackWithoutWait(self):
		while self.logins.hasNext():
			login = self.logins.getNext()
			while self.passwords.hasNext():
				password = self.passwords.getNext()
				self.pattern.doActions(password, login)

	def doAttackWithWait(self):
		trial = 0
		while self.logins.hasNext():
			login = self.logins.getNext()
			while self.passwords.hasNext():
				trial += 1
				password = self.passwords.getNext()
				self.pattern.doActions(password, login, trial)