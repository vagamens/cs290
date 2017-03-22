# import all the things
import sqlite3
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, flash, jsonify
from contextlib import closing
from app.shakespeare.models import Insult, Lines

mod = Blueprint('shakespeare', __name__, url_prefix='/shakespeare',
				template_folder='templates', static_folder='static')

@mod.route("/")
def shakespeare():
	flash("test")
	return render_template("game.html")

@mod.route("/game", methods=['POST', 'GET'])
def game():
	response = {}
	j = request.get_json()
	print j
	response['command'] = j['command']
	if(j['command'] == 'insult'): 
		response['insult'] = Insult.generateInsult()
	elif(j['command'] == 'getFirstScene'):
		response['scene'] = Lines.getScene(1, 1)
		print response['scene']
		response['a'] = 1
		response['s'] = 1
	elif(j['command'] == 'getNextScene'):
		scene = Lines.getNextScene(j['a'], j['s'])
		response['scene'] = scene[2]
		response['a'] = scene[0]
		response['s'] = scene[1]
	print response
	return jsonify(response)