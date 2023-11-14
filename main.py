from pygreen import create_app
from flask import redirect, request, render_template, url_for
import mysql.connector
from flask_hashing import Hashing

app = create_app()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='auth'
)

hashing = Hashing(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    email = request.form.get('email')
    nome = request.form.get('name')
    sobrenome = request.form.get('last-name')
    senha = request.form.get('password')

    hashed_password = hashing.hash_value(senha)
    hashed_password = hashed_password[:16]

    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE email='{email}'")
    fetchdata = cursor.fetchall()
    
    if fetchdata:
        raise Exception("Ei, deu erro... Já tem esse email ó")
    else:
        return redirect(url_for("profile", email=email, nome=nome, sobrenome=sobrenome, hashed_password=hashed_password))

@app.route('/profile', methods=['GET','POST'])
def profile():
    cursor = db.cursor(dictionary=True) 
    email = request.args.get('email')
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    hashed_password = request.args.get('hashed_password')

    post = f"INSERT INTO Pessoa (tipoID, email, nome, sobrenome, senha) VALUES (1, '{email}', '{nome}', '{sobrenome}', '{hashed_password}')"

    cursor.execute(post)
    cursor.close()
    db.commit()
    return redirect('/')


@app.route("/user/<usuario>")
def usuario(usuario):
    
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE usuario='{usuario}'")
    fetchdata = cursor.fetchall()
    try:
        nome = fetchdata[0]['nome']
        pessoaID = fetchdata[0]['pessoaID']
        sobrenome = fetchdata[0]['sobrenome']
    except:
           render_template('404.html')
    return render_template('perfilUsuario.html', usuario = usuario, nome=nome, pessoaID=pessoaID, sobrenome=sobrenome)

@app.route('/login', methods=['GET', 'POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('password')
    
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM Pessoa WHERE usuario='{usuario}'")
    fetchdata = cursor.fetchall()
    
    hashed_password = hashing.hash_value(senha)
    hashed_password = hashed_password[:16]
    
    cursor.execute(f"SELECT senha FROM Pessoa WHERE usuario='{usuario}'")
    fetchdata2 = cursor.fetchall()
    
    if(fetchdata):
        if(hashed_password == fetchdata2[0]["senha"]):
            return redirect(f'/{usuario}')
    else:
        print('nao foi')
        raise Exception("Ei, deu erro, esse usuario nem existe")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)