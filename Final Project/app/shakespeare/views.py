# import all the things
import sqlite3
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, falsh
from contextlib import closing

mod = Blueprint('shakespeare', __name__, url_prefix='shakespeare')

@mod.route("/")
def shakespeare():
	flash("test")
	return render_template("shakespeare/game.html")

@mod.route("/game", methods=['POST'])
def game():
	pass