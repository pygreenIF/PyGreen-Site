from flask import Blueprint, render_template, redirect, request, flash
import mysql.connector

auth = Blueprint("auth", __name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='auth'
)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    email = request.form.get('email')
    nome = request.form.get('name')
    sobrenome = request.form.get('last-name')
    senha = request.form.get('password')
    senha_hashed = hashing.hash_value(senha, salt='utf-8')

    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE email='{email}'")
    fetchdata = cursor.fetchall()

    if(fetchdata):
        raise Exception("Ei, deu erro... Já tem esse email ó")
    else:
        post = f"INSERT INTO Pessoa (tipoID, email, nome, sobrenome, senha) VALUES (1, '{email}', '{nome}', '{sobrenome}', '{senha_hashed}')"
        cursor.execute(post)
        cursor.close()
        db.commit()
        return redirect('/')

@auth.route("/<usuario>")
def usuario(usuario):
    return f"Salve, {usuario}!"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('password')

    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE usuario='{usuario}'")
    fetchdata = cursor.fetchall()

    if(fetchdata):
        if(senha == cursor.execute(f"SELECT senha FROM Pessoa WHERE usuario='{usuario}'")):
            return redirect(f'/{usuario}')
    else:
        raise Exception("Ei, deu erro, esse usuario nem existe")

