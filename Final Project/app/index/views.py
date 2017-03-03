# import all the things
from flask import Blueprint, request, session
from flask import g, redirect, url_for, abort
from flask import render_template, falsh
from contextlib import closing

mod = Blueprint('', __name__, url_prefix='')

@mod.route("/")
def index():
	return redirect("shakespeare.shakespeare")
