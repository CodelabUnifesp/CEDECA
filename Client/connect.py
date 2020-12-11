import pymongo
from pymongo import MongoClient

#Para compilar é preciso algumas ferramentas:
#- instalar mongoDB (nao é necessario instalar o 'mongo compass'. Caso queira, pode instalar, mas é demorado)
#- pip install pymongo
#- pip install dnspython
#se no windows o comando mongo não for reconhecido após a instalacao, é só mapear a variável de ambiente. 

class connectMongo:

    def __init__(self):
        print("Iniciando conexao...\n")
        #conecta ao banco de dados
        self.client = pymongo.MongoClient("mongodb+srv://codelabCEDECA:ziviani123@codelabcedeca-vmemm.mongodb.net/test?retryWrites=true")
        print("Conectado ao MongoDB\n")   
        #base de dados 
        self.db = self.client.cedeca #cedeca eh o nome do database a ser utilizado
        self.collection = self.db.pessoas #pessoas eh o nome do collection
        #collection eh como se fosse a tabela de um banco SQL
        #para criar novas collection eh so mudar de 'pessoas' para qlqr outro nome
        #o uso de collections seria semelhante a de tabelas
        #Por exemplo, um collection para pessoas, outro para processos...

    #define qual collection ira utilizar
    def criarConexao(self, col):
        self.collection = self.db[col]

    #podemos criar um inserir para cada collection
    def inserir(self, name, CPF):
        print("Inserindo dados...\n")
        self.collection.insert_one( {
            "name" : name,
            "CPF" : CPF
            }) #add a document

    def exibir(self):
        print("Exibindo dados:\n")
        #self.collection.find({},{"name":1, "_id":0}) #retorna apenas o campo "name"
        #self.collection.find({"name":"joao"}) #retorna todos com o "name" igual a "joao"
        result = self.collection.find() #eh possivel armazenar o resultado da query em uma variavel
        #for doc in self.collection.find(): #tambem eh possivel fazer desse modo
        for doc in result:
            print(doc)
        print("\n")

    def removerTudo(self):
        print("Removendo dados...\n")
        result = self.collection.find() #seria possivel retornar 'result'
        for doc in result:  
            text = str(doc['name']) #obter um campo especifico de um objeto
            print(text)             #seria possivel retornar 'result' e utilizar os valores nas outras telas
            self.collection.delete_one(doc)

####### Para Testes ##############
mongo = connectMongo()
mongo.criarConexao("pessoas")
mongo.inserir("joao", "123.456.789-23")
mongo.inserir("roberta", "123.456.789-23")
mongo.exibir()
mongo.removerTudo() #removo todos para limpar o banco
#####################################

print("\nConcluido!")