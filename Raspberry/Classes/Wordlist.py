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
		
class BruteforceMultipleSize:
	def __init__(self, charset_name, size_min, size_max):
		self.charset = self.getCharset(charset_name)
		self.BF = Bruteforce(self.charset, size_min)
		self.size = size_min
		self.max = size_max
		
	def getCharset(self, charset_name):
		if charset_name == 'numeric':
			return "0123456789"
		elif charset_name == 'alphalower':
			return "abcdefghijklmnopqrstuvwxyz"
		elif charset_name == 'alphaupper':
			return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		elif charset_name == 'alpha':
			return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		elif charset_name == 'alphanumericlower':
			return "abcdefghijklmnopqrstuvwxyz0123456789"
		elif charset_name == 'alphanumericupper':
			return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		elif charset_name == 'alphanumeric':
			return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
			
	def getNext(self):
		if self.BF.hasNext() is False:
			self.size += 1
			self.BF = Bruteforce(self.charset, self.size)
		
		return self.BF.getNext()
			
	def hasNext(self):
		if self.BF.hasNext():
			return True
		else:
			return self.size < self.max

class Bruteforce:

	# Brute-force string generation
	# Copyright (C) 2011 Radek Pazdera
	# From https://gist.github.com/pazdera/1121315
	# Turned into a Class by Antoine Cervoise 2016

	# This program is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.

	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	# GNU General Public License for more details.

	# You should have received a copy of the GNU General Public License
	# along with this program. If not, see <http://www.gnu.org/licenses/>.


	def __init__(self, charset, size):
		self.charset = charset
		self.number_of_characters = len(self.charset)
		self.size = size
		self.bruteforce = list()

	def characterToIndex(self, char):
	    return self.charset.index(char)

	def indexToCharacter(self, index):
	    if self.number_of_characters <= index:
		raise ValueError("Index out of range.")
	    else:
		return self.charset[index]

	def hasNext(self):
		local = list(self.bruteforce)
		return len(self.next(local)) == self.size

	def getNext(self):
		self.bruteforce = self.next(self.bruteforce)
		bfstring = ""
		for elmt in self.bruteforce:
			bfstring += str(elmt)
		return bfstring
		
	def next(self, string):
		if len(string) <= 0:
        		for i in range(self.size):
	        		string.append(self.indexToCharacter(0))
    		else:
		    	string[0] = self.indexToCharacter((self.characterToIndex(string[0]) + 1) % self.number_of_characters)
			if self.characterToIndex(string[0]) is 0:
				return list(string[0]) + self.next(string[1:])
		return string