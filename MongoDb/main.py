from src.data import Data

class DataApplication:
    """Aplicação principal para o gerenciamento de dados.

    Esta aplicação utiliza a classe Data para gerenciar as operações de entrada
    e saída de dados, permitindo que o usuário realize ações como salvar, recuperar
    e excluir dados.

    Attributes:
        beginning: Instância da classe Data responsável pelo gerenciamento de dados.
    """

    def __init__(self):
        """Inicializa a aplicação.

        Cria uma instância da classe Data para gerenciar as operações de entrada e saída de dados.
        """
        self.beginning = Data()

    def run(self):
        """Executa a aplicação.

        Controla o fluxo da aplicação, chamando o método controller da instância de Data até que
        o usuário escolha sair.

        Returns:
            None
        """
        start = self.beginning.controller()

        while start:
            start = self.beginning.controller()

        del self.beginning

if __name__ == "__main__":
    app = DataApplication()
    app.run()
