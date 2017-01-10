import os
import sys

from flask import Flask, jsonify, make_response, render_template

app = Falsk(__name__)
app.config.from_object('config')

def installSecretKey(app, filename='secret_key'):
	"""Configure the SECRET_KEY from a file
	   in the instance directory.

	   If the file does not exist, print instructions
	   to create it from a shell with a random key,
	   then exit.
	"""
	filename = os.path.join(app.instace_path, filename)

	try:
		app.config['SECRET_KEY'] = open(filename, 'rb').read()
	except IOError:
		print('Error: No secret key. Create it with:')
		fullPath = os.path.dirname(filename)
		if not os.path.isdir(fullPath):
			print('mkdir -p {filename}'.format(filename=fullPath))
		print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
		sys.exit(1)

if not app.config['DEBUG']
	installSecretKey(app)

from app.index.views import mod as indexModule
app.register_blueprint(indexModule)

from app.users.views import mod as userModule
app.register_blueprint(userModule)

@app.errorhandler(404)
def notFound(error):
	return render_template("404.html")
