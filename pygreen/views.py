from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("home.html", title="Página Principal")

@views.route('/curso')
def curso():
    return render_template("curso.html", title="Curso")

@views.route('/signup')
def signup():
    return render_template("signup.html", title="Cadastrar-se")

@views.route('/signin')
def signin():
    return render_template("loginMobile.html", title="Entrar")

@views.route('/chaveAcesso')
def chaveAcesso():
    return render_template("chaveAcesso.html", title="Chave de acesso")

@views.route('/sobre')
def sobre():
    return render_template("sobre.html", title="Sobre")

@views.route('/paisoncode')
def jogo():
    return render_template("jogo.html", title="Paison Code")