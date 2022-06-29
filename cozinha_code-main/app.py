import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
        connection = get_db_connection()
        post = connection.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone()
        connection.close()
        if post is None:
            abort(404)
        return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'UNIVESP2004525'


@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/cards')
def cards():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('cards.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        estado = request.form['estado']
        cidade = request.form['cidade']
        rua = request.form['rua']
        numero = request.form['numero']
        telefone = request.form['telefone']
        email = request.form['email']
        redes = request.form['redes']
        conteudo = request.form['conteudo']
        username = request.form['username']
        password = request.form['password']
        foto = request.form['foto']
        if not nome:
            flash('Digite o nome da instituição')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                         (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto))
            connection.commit()
            connection.close()
            return redirect(url_for('cards'))
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        estado = request.form['estado']
        cidade = request.form['cidade']
        rua = request.form['rua']
        numero = request.form['numero']
        telefone = request.form['telefone']
        email = request.form['email']
        redes = request.form['redes']
        conteudo = request.form['conteudo']
        username = request.form['username']
        password = request.form['password']
        foto = request.form['foto']
        if not nome:
            flash('Digite o nome da instituição')
        else:
            connection = get_db_connection()
            connection.execute('UPDATE posts SET nome = ?, tipo = ?, estado = ?, cidade = ?, rua = ?, numero = ?, telefone = ?, email = ?, redes = ?, conteudo = ?, username = ?, password = ?, foto = ?'
                         'WHERE id = ?',
                         (nome, tipo, estado, cidade, rua, numero, telefone, email, redes, conteudo, username, password, foto, id))
            connection.commit()
            connection.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=['POST',])
def delete(id):
    post = get_post(id)
    connection = get_db_connection()
    connection.execute('DELETE FROM posts WHERE id = ?', (id,))
    connection.commit()
    connection.close()
    flash('"{}" foi deletado com sucesso'.format(post['nome']))
    return redirect(url_for('index'))


@app.route('/sobre')
def sobre():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('sobre.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor()

        post = cursor.execute("SELECT username, password FROM posts WHERE username = '"+username+"' and password='"+password+"'").fetchall()
        connection.close()

        if len(post) == 0:
            flash('Usuário ou senha inválidos')
        else:
            connection = get_db_connection()
            post = connection.execute('SELECT * FROM posts WHERE username = ?', (username,)).fetchone()
            connection.commit()
            connection.close()
            return render_template('home.html', post=post)
    return render_template('login.html')


@app.route('/logout')
def logout():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('sobre.html', posts=posts)