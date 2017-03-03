# import all the things
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, flash
from contextlib import closing

mod = Blueprint('index', __name__, url_prefix='')

@mod.route("/")
def index():
	return redirect(url_for("shakespeare.shakespeare"))
