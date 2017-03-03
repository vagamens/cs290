#!/bin/env python3
import os
import platform

def main():
	if (platform.system() == 'Linux') :
		os.system("sudo pip install flask")
		os.system("sudo pip install flask-wtf")
	else:
		os.system("pip install flask")
		os.system("pip install flask-wtf")

	f = False
	wtf = False

	try:
		from flask import Flask
		f = True
	except:
		f = False

	try:
		from flask.ext.wtf import Form
		wtf = True
	except:
		wft = False

	if (f and wtf) :
		print("You are good to go. Just run the run.py file to run the server")
	elif (f and not wtf) :
		print("Flask is goo to go, but the wtforms integration is stuck.")
		print("Just rerun this file to get it installed")
	elif (not f):
		print("Flask failed to install.\nYou can either rerun this file")
		print("run the commands yourself")
		print("On Windows:\nopen the command line and type:\npip install flask")
		print("pip install flask-wtf")

if __name__ == '__main__':
	main()