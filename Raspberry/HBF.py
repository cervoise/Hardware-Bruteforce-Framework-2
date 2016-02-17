import argparse
import commands
import os
import sys
import time

from Classes import Action
from Classes import Analyzer
from Classes import Attack
from Classes import Keyboard
from Classes import Wordlist

DEBUG = False

def main():
	global DEBUG

	parser = argparse.ArgumentParser(description='HBF Description')

	parser.add_argument('pattern', help='Attack pattern file')
	parser.add_argument('-p','--passwordsFile', help='Passwords file (one password by line)', default='', required=False)
	parser.add_argument('-l','--loginsFile', help='Logins file (one login by line)', default='', required=False)
	parser.add_argument('-s','--screenshots', help='Directory to put the screenshots (created if don\'t exist)', default='', required=False)
	parser.add_argument('--noScreenshots', help='Ignore screenshot command', action='store_true')

	args = vars(parser.parse_args())

	if args['screenshots'] != '' and args['noScreenshots'] is True:
		print "A screenshots folder is specify as the --noScreenshots option"
		sys.exit(1)

	#Add to help/usage: 
	#Read ../readme.txt before run
	#Edit attack in order to add -d

	HBF = Attack.Attack(args['pattern'], args['loginsFile'], args['passwordsFile'], args['screenshots'], args['noScreenshots'], DEBUG)
	HBF.doAttack()

if __name__ == "__main__":
    main()