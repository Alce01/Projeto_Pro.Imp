from flask import Blueprint

views = Blueprint("views")

@views.route("/")
def home():
    return "home page"

if __name__ == '__main__':
    views.run(debug=True, port=8000)