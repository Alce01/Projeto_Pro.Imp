from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True, user="Usuário", password="Senha")

@auth.route('/logout')
def logout():
    redirect(url_for("home.get_json"))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('fisrtName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) > 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        else:
            # add user to database
            pass

    return render_template("sign_up.html")