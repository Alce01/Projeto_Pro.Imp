from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
    data = request.form
    print(data)
    return render_template("login.html", boolean=True, user="Usuário", password="Senha")

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 5:
            flash('O email deve ter mais de 5 caracteres', category='error')
            pass
        elif len(firstName) < 2:
            flash('Seu nome deve ter mais de 2 caracteres', category='error')
        elif password1 != password2:
            flash('A senha não é a mesma', category='error')
        elif len(password1) != 12:
            flash('A senha deve ter 12 números', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")