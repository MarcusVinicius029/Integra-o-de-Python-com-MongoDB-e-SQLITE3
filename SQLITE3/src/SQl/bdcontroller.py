import sqlite3
import os

"""Classe para gerenciar a conexão com o banco de dados SQLite.

    Attributes:
        con (sqlite3.Connection): A conexão com o banco de dados SQLite.
        cursor (sqlite3.Cursor): O cursor para executar operações no banco de dados.
"""


class Connection:
    def __init__(self, path):
        """Inicializa a conexão com o banco de dados SQLite.

        Obs: O caminho indicado pode necessitar de alterações.

        Se o arquivo do banco de dados existe, cria a conexão e o cursor.
        Caso contrário, cria o diretório e o arquivo do banco de dados, e em seguida, a conexão e o cursor.
        """
        if os.path.exists(path):
            joinedpath = os.path.join(path)
            self.con = sqlite3.connect(joinedpath)
            self.cursor = self.con.cursor()
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            self.con = sqlite3.connect(path)
            self.cursor = self.con.cursor()
    
    def create_tables(self):
        """Cria a tabela 'User' caso ela não exista."""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User (nome text, idade integer, cpf integer)")
        self.con.commit()

    def get_data(self, cpf):
        """Recupera dados do banco de dados com base no CPF.

        Args:
            cpf (int): O CPF a ser pesquisado.

        Returns:
            tuple: Uma tupla contendo os dados (nome, idade) se encontrados, caso contrário, None.
        """
        self.cursor.execute("SELECT nome, idade FROM User WHERE cpf = ?",(cpf, ))
        results = self.cursor.fetchone()
        return results
    
    def insert_data(self, nome, idade, cpf):
        """Insere dados na tabela 'User'.

        Args:
            nome (str): O nome a ser inserido.
            idade (int): A idade a ser inserida.
            cpf (int): O CPF a ser inserido.
        """
        self.cursor.execute("INSERT INTO User VALUES (?, ?, ?)", (nome, idade, cpf,))
        self.con.commit()

    def delete_data(self, cpf):
        """Exclui dados da tabela 'User' com base no CPF.

        Args:
            cpf (int): O CPF a ser excluído.
        """
        self.cursor.execute("DELETE FROM User WHERE cpf = ?", (cpf,))
        self.con.commit()

    def __del__(self):
        """Fecha a conexão com o banco de dados ao destruir a instância da classe."""
        self.con.close()