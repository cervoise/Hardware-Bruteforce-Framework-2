import commands
import os.path 

class Analyzer:
	def __init__(self, path_to_samples, path_to_screenshots, passwords_file):
		self.screenshots_samples =  []
		for root, dirs, files in os.walk(path_to_samples):  
			for i in files:  
				self.screenshots_samples.append(os.path.join(i))  

		self.passwords = []
		for elmt in open(passwords_file).readlines():
	        	self.passwords.append(elmt.rstrip())
	        	
	        self.comparaisons = []
	        for password in self.passwords:
	        	temp_samples = []
        		for sample in self.screenshots_samples:
        			temp_samples.append(self.compare(path_to_screenshots + '/' + password + ".jpg", path_to_samples + '/' + sample))
        		self.comparaisons.append(Comparaison(password, temp_samples))
	
	def compare(self, sample, screenshot):
		compare_command_line = 'compare -metric RMSE "' + sample + '" "'
                compare_command_line += screenshot + '" NULL'
                return commands.getstatusoutput(compare_command_line)[1].split('(')[1][:-1]
        
        			
        def getStats(self):
        	#One entry for each sample
        	medium_array = []
        	max_array = []
        	min_array = []
        	for sample in self.screenshots_samples:
        		medium_array.append(0)
        		max_array.append(0)
        		min_array.append(1.00)
        	
        	for comparaison in self.comparaisons:
        		for i in range(0, len(self.screenshots_samples)):
        			medium_array[i] += float(comparaison.getSamples()[i])
        			if float(comparaison.getSamples()[i]) > max_array[i]:
        				max_array[i] = float(comparaison.getSamples()[i])
        			if float(comparaison.getSamples()[i]) < min_array[i]:
        				min_array[i] = float(comparaison.getSamples()[i])
        				
        	csv = "average;"
        	for elmt in medium_array:
        		csv += str(elmt/len(self.passwords)) + ";"
        	csv += "\n"
        	
        	csv += "max;"
        	for elmt in max_array:
        		csv += str(elmt) + ";"
        	csv += "\n"
        	
        	csv += "min;"
        	for elmt in min_array:
        		csv += str(elmt) + ";"
        	csv += "\n"
        	
        	return csv
        	
        def getCsv(self):
        	csv = "Password;"
        	for sample in self.screenshots_samples:
        		csv += sample + ";"
        	csv += "\n"
        	for comparaison in self.comparaisons:
        		csv += comparaison.getCsvLine()
        	
        	csv += self.getStats()
        	
        	return csv
        
        def writeCsv(self, path_to_csv):
        	csv_file = open(path_to_csv, 'w+')
        	csv_file.write(self.getCsv())
        	csv_file.close()
        
class Comparaison:
	def __init__(self, password, samples_array):
		self.password = password
		self.samples = []
		for elmt in samples_array:
			self.samples.append(elmt)
	
	def getPassword(self):
		return self.password
	
	def getSamples(self):
		return self.samples
	
	def getCsvLine(self):
		csv_line = self.password + ";"
		for sample in self.getSamples():
			csv_line += sample + ";"
		return csv_line + "\n"
