from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/curso')
def curso():
    return render_template("curso.html")

@views.route('/signup')
def signup():
    return render_template("signup.html")

@views.route('/signin')
def signin():
    return render_template("loginMobile.html")

@views.route('/chaveAcesso')
def chaveAcesso():
    return render_template("chaveAcesso.html")