class EmptyWordlist():
	def __init__(self):
		self.loop = 0
		self.wordlist_array = [""]
		
	def hasNext(self):
		return self.loop < len(self.wordlist_array)
	
	def getNext(self):
		if self.loop == len(self.wordlist_array):
			return False
		self.loop += 1
		return self.wordlist_array[self.loop-1]

class Wordlist(EmptyWordlist):
	def __init__(self, path_to_wordlist):
		self.loop = 0
		self.wordlist_array = []
		for line in open(path_to_wordlist).readlines():
			self.wordlist_array.append(line.rstrip())
		
#A faire
class BruteforceArray():
	def __init(self, chars_array, size_min, size_max):
		return ""
	
	def getNext(self):
		return ""
		
	def hasNext(self):
		return ""

#Inutile si la classe precedente est bien faite			
class BruteforcePin():
	def __init(self, size_min, size_max):
		return ""

	def getNext(self):
		return ""

	def hasNext(self):
		return ""
