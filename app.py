from flask import Flask, render_template, request
from module import insere_dados

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def envia_dados():
    nome = request.args.get('nome')
    email = request.args.get('email')
    endereco = request.args.get('endereco')
    if request.form.get('envio') == 'enviar':
        insere_dados(nome, email, endereco)  
app.run(debug = True)