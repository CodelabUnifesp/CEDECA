from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://japznbipnbuvjt:a2235c2bf5338755d5ae1fae192890f789c273e995e46ae568d494b382910df7@ec2-34-200-181-5.compute-1.amazonaws.com:5432/d73bllgnm0jg3b"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Endereco(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(10), unique=False, nullable=False)
    cidade = db.Column(db.String(100), unique=False, nullable=False)
    estado = db.Column(db.String(2), unique=False, nullable=False)
    rua = db.Column(db.String(120), unique=False, nullable=False)
    numero = db.Column(db.Integer, unique=False, nullable=False)
    bairro = db.Column(db.String(120), unique=False, nullable=False)
    complemento = db.Column(db.String(120), unique=False, nullable=False)
    def __init__(self, cep, cidade, estado, rua, numero, bairro, complemento):
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento

class Assistido(db.Model):
    __tablename__ = "assistido"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    nacionalidade = db.Column(db.String(30), unique=True, nullable=False)
    estado_civil = db.Column(db.String(20), unique=True, nullable=False)
    profissao = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=False, nullable=False)
    rg = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)
    def __init__(self, nome, nacionalidade, estado_civil, profissao, cpf, rg, telefone, email, endereco):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class ParteContraria(db.Model):
    __tablename__ = "partecontraria"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=False, nullable=False)
    nacionalidade = db.Column(db.String(120), unique=False, nullable=False)
    estado_civil = db.Column(db.String(120), unique=False, nullable=False)
    profissao = db.Column(db.String(120), unique=False, nullable=False)
    cpf = db.Column(db.String(14), unique=False, nullable=False)
    rg = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)
    def __init__(self, nome, nacionalidade, estado_civil, profissao, cpf, rg, telefone, email, endereco):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Crianca(db.Model):
    __tablename__ = "crianca"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=False, nullable=False)
    nascimento = db.Column(db.String(10), unique=False, nullable=False)
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

class Testemunha(db.Model):
    __tablename__ = "testemunha"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=False, nullable=False)
    cpf = db.Column(db.String(14), unique=False, nullable=False)
    rg = db.Column(db.String(14), unique=True, nullable=False)
    endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)
    def __init__(self, nome, cpf, rg, endereco):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco

class TestemunhasAtendimento(db.Model):
    __tablename__ = "testemunhasatendimento"
    id = db.Column(db.Integer, primary_key=True)
    testemunha = db.Column(db.Integer, db.ForeignKey('testemunha.id'), nullable=False)
    atendimento = db.Column(db.Integer, db.ForeignKey('atendimento.id'), nullable=False)
    def __init__(self, testemunha, atendimento):
        self.testemunha = testemunha
        self.atendimento = atendimento

class CriancasAtendimento(db.Model):
    __tablename__ = "criancasatendimento"
    id = db.Column(db.Integer, primary_key=True)
    crianca = db.Column(db.Integer, db.ForeignKey('crianca.id'), nullable=False)
    atendimento = db.Column(db.Integer, db.ForeignKey('atendimento.id'), nullable=False)
    def __init__(self, crianca, atendimento):
        self.crianca = crianca
        self.atendimento = atendimento

class Atendimento(db.Model):
    __tablename__ = "atendimento"
    id = db.Column(db.Integer, primary_key=True)
    assistido = db.Column(db.Integer, db.ForeignKey('assistido.id'), nullable=False)
    parte_contraria = db.Column(db.Integer, db.ForeignKey('partecontraria.id'), nullable=False)
    data_registro = db.Column(db.DateTime, nullable=False)
    def __init__(self, assistido, parte_contraria, criancas, testemunhas):
        import datetime
        self.assistido = assistido
        self.parte_contraria = parte_contraria
        self.criancas = criancas
        self.testemunhas = testemunhas
        self.data_registro = datetime.datetime.now()
