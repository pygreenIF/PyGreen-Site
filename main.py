from pygreen import create_app
from flask import redirect, request
import mysql.connector

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='auth'
)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    email = request.form.get('email')
    nome = request.form.get('name')
    sobrenome = request.form.get('last-name')
    senha = request.form.get('password')

    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE email='{email}'")
    fetchdata = cursor.fetchall()

    if(fetchdata):
        raise Exception("Ei, deu erro... Já tem esse email ó")
    else:
        post = f"INSERT INTO Pessoa (tipoID, email, nome, sobrenome, senha) VALUES (1, '{email}', '{nome}', '{sobrenome}', '{senha}')"
        cursor.execute(post)
        cursor.close()
        db.commit()
        return redirect('/')

@app.route("/<usuario>")
def usuario(usuario):
    return f"Salve, {usuario}!"

@app.route('/login', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)