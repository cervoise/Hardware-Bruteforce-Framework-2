import time
import os
import commands

from Classes import Action
from Classes import Attack
from Classes import Keyboard
from Classes import Wordlist
		
passfile = "passwords.txt"
HBF = Attack.Attack("test.txt", "wait.txt", "logins.txt", passfile)
HBF.doAttack()

screenshots_temoins = ["temoin1", "temoin2"]

csv_compare = "Password;"
for temoin in screenshots_temoins:
	csv_compare += temoin + ";"
csv_compare += "\n"

for elmt in passfile:
	csv_compare += elmt + ";"
	for temoin in screenshots_temoins:
		compare_command_line = 'compare -metric RMSE screenshots/' + temoin + '.jpg screenshots/' + elmt + '.jpg NULL'
		csv_compare += commands.getstatusoutput(compare_command_line)[1].split('(')[:-1]
		csv_compare += ";"
	csv_compare += "\n"
	
csv_result = open('result.txt', 'a+')
csv_result.write(csv_compare)
csv_result.close()
