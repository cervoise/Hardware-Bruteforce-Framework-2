#code from http://wemo.forumatic.com/viewtopic.php?f=2&t=5

import os

path = os.path.dirname(os.path.realpath(__file__))
command_line = 'bash ' + path + '/wemo-on-off.sh '


def on(IP):
	os.system(command_line + IP + " ON")

def off(IP):
	os.system(command_line + IP + " OFF")
