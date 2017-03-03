# import all the things
import sqlite3
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, falsh
from contextlib import closing

mod = Blueprint('index', __name__, url_prefix='')

@mod.route("/")
def index():
	flash("test")
	return render_template("index/index.html")
