import pymongo as py

"""Módulo de Conexão com MongoDB.

    Este módulo contém a classe Connection, que é responsável por iniciar
    a conexão com o MongoDB e fornecer acesso ao banco de dados e à coleção
    interna onde os dados serão armazenados.

    Returns:
        cliente: Objeto MongoClient que representa a conexão com o MongoDB.
        db: Objeto que aponta para o banco de dados MongoDB.
        dados: Objeto que aponta para a coleção interna onde os dados serão armazenados.
"""
class Connection:
    def __init__(self):
        """Inicializa a classe e configura a conexão
            Função de inicialização da classe Connection. Aqui são criadas as
            variáveis cliente, db e dados para a configuração do ambiente de
            conexão com o Mongo Db
        """

        self.cliente = py.MongoClient("mongodb+srv://mvb0293:marcus@cluster1.nm3oziv.mongodb.net/")
        self.db = self.cliente.users
        self.dados = self.db.dados

    def getInformation(self):
        """Repassa informações sobre a conexão
            
        Returns:
            db = Variável que aponta para o banco de dados 
            dados = Variável que aponta para a coleção
        """
        return self.db, self.dados
    
    def __del__(self):
        """Fecha a conexão com o banco de dados e exclui o objeto 
        """
        self.cliente.close()

