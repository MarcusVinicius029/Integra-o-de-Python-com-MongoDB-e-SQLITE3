from src.connection import Connection
from src.screen import Screen

"""Módulo de Gerenciamento de Entradas e Saídas de Dados.

    Este módulo contém a classe Data, que é responsável por gerenciar
    as entradas e saídas de dados interagindo com a classe Screen para
    obter informações do usuário e com a classe Connection para interagir
    com o banco de dados.

    Attributes:
        screen: Instância da classe Screen responsável pela interação com o usuário.
        _db: Objeto que aponta para o banco de dados MongoDB.
        dados: Objeto que aponta para a coleção interna onde os dados serão armazenados.
"""

class Data:
    def __init__(self):
        """Inicializa a classe Data.

        Cria instâncias das classes Screen e Connection para gerenciar
        a interação com o usuário e a conexão com o banco de dados.
        """
        self.screen = Screen()
        con = Connection()
        self._db, self.dados = con.getInformation()

    def controller(self):
        """Controla o fluxo de operações com base nas entradas do usuário.

        Retorna True se as operações foram concluídas com sucesso ou False
        se o usuário escolheu sair.

        Returns:
            bool: Indica se as operações foram concluídas ou se o usuário escolheu sair.
        """
        _i = self.screen.mainscreen()

        if _i == 1:
            _nome, _idade, _cpf = self.screen.insertdata()

            dado = {
                "nome": _nome,
                "idade": _idade,
                "cpf": _cpf
            }

            self._db.self.dados.insert_one(dado)
            print("Inserção concluída!")
            return True

        elif _i == 2:
            _cpf = self.screen.rescuedata()
            document = self._db.self.dados.find_one({"cpf" : _cpf})
            if document != None:
                print(document)
            else:
                print("Dados não encontrados!")
            return True
        elif _i == 3:
            _cpf = self.screen.deletedata()
            self._db.self.dados.delete_one({"cpf":_cpf})
            print("Dados deletados com sucesso")
            return True
        elif _i == 00:
            return False