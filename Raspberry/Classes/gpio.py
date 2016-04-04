#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Needs to be launched as root

import argparse
import time
import RPi.GPIO as GPIO


parser = argparse.ArgumentParser(description='Set a GPIO output to high for a given time')
parser.add_argument('pin', metavar='pin', type=int, help='The pin (BCM mode)')
parser.add_argument('time', metavar='time', type=float, help='Time in seconds (float value)')
args = parser.parse_args()

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(args.pin, GPIO.OUT, initial=GPIO.HIGH)
	time.sleep(args.time)
	GPIO.output(args.pin, GPIO.LOW)
	GPIO.cleanup(args.pin)
	
except KeyboardInterrupt:
	GPIO.cleanup(args.pin)

