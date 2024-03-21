from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/profile')
@login_required
def profile():
    user_password = session.get('user_password')
    password = session.get('password')

    session['password'] = password

    return render_template("profile.html", user=current_user, password=user_password)

@views.route('/pacientes')
@login_required
def pacientes():
    user_password = session.get('user_password')
    password = session.get('password')

    session['password'] = password

    return render_template("pacientes.html", user=current_user, password=user_password)

@views.route('/exames', methods=['GET', 'POST'])
def exames():
    return render_template('exames.html')

