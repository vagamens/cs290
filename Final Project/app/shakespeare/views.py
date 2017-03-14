# import all the things
import sqlite3
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, flash, jsonify
from contextlib import closing
from app.models import Insult

mod = Blueprint('shakespeare', __name__, url_prefix='/shakespeare',
				template_folder='templates', static_folder='static')

@mod.route("/")
def shakespeare():
	flash("test")
	return render_template("game.html")

@mod.route("/game", methods=['POST', 'GET'])
def game():
	response = {}
	print request.get_json()
	j = request.get_json()
	print j
	print type(j)
	response['command'] = j['command']
	if(j['command'] == 'insult'): 
		response['insult'] = Insult.generateInsult()
	print response
	return jsonify(response)