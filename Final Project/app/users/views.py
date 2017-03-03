from flask import Blueprint, request, render_template, flash, g, session, redirect
from flask import url_for
from werkzeug import check_password_hash, generate_password_hash

#from app import db
from app.users.models import User
from app.users.decorators import requiresLogin

mod = Blueprint('user', __name__, url_prefix='/student')

@mod.route('/')
#@requiresLogin
def home():
	return redirect(url_for('users.profile'))
	#return render_template("students/dashboard.html")#, user=g.user)

@mod.route('/dashboard')
#@requiresLogin
def dashboard():
	flash("test")
	return render_template("users/profile.html")#, user=g.user)
