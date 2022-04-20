from flask import Flask, render_template, request, redirect, config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'


class Pessoa(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    endereco = db.Column(db.String)

    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        endereco = request.form.get('endereco')

        if nome and email and endereco:
            p = Pessoa(nome, email, endereco)
            db.session.add(p)
            db.session.commit()

    return redirect('/')


@app.route('/lista')
def lista():
    pessoas = Pessoa.query.all()
    return render_template('lista.html', pessoas=pessoas)


@app.route('/apagar/<int:id>')
def excluir(id):
    pessoa = Pessoa.query.filter_by(id=id).first()

    db.session.delete(pessoa)
    db.session.commit()

    pessoas = Pessoa.query.all()
    return render_template("lista.html", pessoas=pessoas)


if __name__ == '__main__':
    app.run(debug=True)
