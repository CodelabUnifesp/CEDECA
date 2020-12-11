from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class assistido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    nacionalidade = db.Column(db.String(120), unique=True, nullable=False)
    estado_civil = db.Column(db.String(120), unique=True, nullable=False)
    profissao = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(120), unique=True, nullable=False)
    rg = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(120), unique=True, nullable=False)
    cep = db.Column(db.String(120), unique=True, nullable=False)
    cidade = db.Column(db.String(120), unique=True, nullable=False)
    estado = db.Column(db.String(120), unique=True, nullable=False)
    rua = db.Column(db.String(120), unique=True, nullable=False)
    numero = db.Column(db.String(120), unique=True, nullable=False)
    bairro = db.Column(db.String(120), unique=True, nullable=False)
    complemento = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class parte_contraria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    nacionalidade = db.Column(db.String(120), unique=True, nullable=False)
    estado_civil = db.Column(db.String(120), unique=True, nullable=False)
    profissao = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(120), unique=True, nullable=False)
    rg = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(120), unique=True, nullable=False)
    cep = db.Column(db.String(120), unique=True, nullable=False)
    cidade = db.Column(db.String(120), unique=True, nullable=False)
    estado = db.Column(db.String(120), unique=True, nullable=False)
    rua = db.Column(db.String(120), unique=True, nullable=False)
    numero = db.Column(db.String(120), unique=True, nullable=False)
    bairro = db.Column(db.String(120), unique=True, nullable=False)
    complemento = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class crianca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    nascimento = db.Column(db.String(120), unique=True, nullable=False)

class testemunha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    cpf = db.Column(db.String(120), unique=True, nullable=False)
    rg = db.Column(db.String(80), unique=True, nullable=False)
    cep = db.Column(db.String(80), unique=True, nullable=False)
    rua = db.Column(db.String(80), unique=True, nullable=False)
    numero = db.Column(db.String(80), unique=True, nullable=False)
    bairro = db.Column(db.String(80), unique=True, nullable=False)
    cidade = db.Column(db.String(80), unique=True, nullable=False)
    estado = db.Column(db.String(80), unique=True, nullable=False)

class atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assistido = db.Column(db.String(80), unique=True, nullable=False)
    testemunha = db.Column(db.String(120), unique=True, nullable=False) #Relação de várias testemunhas, fazer outra tabela
    parte_contraria = db.Column(db.String(120), unique=True, nullable=False)
    criancas = db.Column(db.String(120), unique=True, nullable=False) #Relação de várias crianças, fazer outra tabela

    def __repr__(self):
        return '<User %r>' % self.username