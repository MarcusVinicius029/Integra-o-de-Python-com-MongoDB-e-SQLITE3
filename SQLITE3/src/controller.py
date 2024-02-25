from src.SQl.bdcontroller import Connection
from src.screen import Screen

"""Controlador principal para interação entre usuário e banco de dados.

    Esta classe utiliza instâncias da classe Connection para manipular operações
    de banco de dados e instâncias da classe Screen para interação com o usuário.

    Attributes:
        connection: Instância da classe Connection para manipulação do banco de dados.
        screen: Instância da classe Screen para interação com o usuário.
        _i: Escolha do usuário.

    Methods:
        __init__(): Inicializa o controlador, criando instâncias da classe Connection e Screen.

        start_controller(): Inicia o controlador, exibindo a tela principal e realizando a operação escolhida pelo usuário.

        Returns:
            bool: Retorna True se o controlador deve continuar a execução, False se deve ser encerrado.
"""


class Controller:
    def __init__(self, path):
        """Inicializa o controlador, criando instâncias da classe Connection e Screen."""
        self.connection = Connection(path)
        self.connection.create_tables()
        self.screen = Screen()

    def start_controller(self):
        """Inicia o controlador, exibindo a tela principal e realizando a operação escolhida pelo usuário.

        Returns:
            bool: Retorna True se o controlador deve continuar a execução, False se deve ser encerrado.
        """
        self._i = self.screen.main_screen()
        if self._i == 1:
            _nome, _idade, _cpf = self.screen.save_data()
            self.connection.insert_data(_nome, _idade, _cpf)
            print("Dados inseridos com sucesso!")
            return True
        elif self._i == 2:
            _cpf = self.screen.get_data()
            results = self.connection.get_data(_cpf)
            print(results)
            return True
        elif self._i == 3:
            _cpf = self.screen.delete_data()
            self.connection.delete_data(_cpf)
            print("Dado deletado com sucesso!")
            return True
        elif self._i == 00:
            return False
