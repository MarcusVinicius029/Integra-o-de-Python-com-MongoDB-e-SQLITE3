"""Classe de Interface do Usuário.

    Esta classe fornece métodos para interação com o usuário, como exibir
    telas principais e obter dados inseridos pelo usuário.

    Methods:
        mainscreen(): Exibe a tela principal e retorna a escolha do usuário.
        insertdata(): Solicita ao usuário que insira dados e retorna as informações fornecidas.
        rescuedata(): Solicita ao usuário um CPF para buscar dados e retorna o valor inserido.
        deletedata(): Solicita ao usuário um CPF para excluir dados e retorna o valor inserido.
"""
class Screen:
    def mainscreen(self):
        """Exibe a tela principal e obtém a escolha do usuário.

        Returns:
            int: Escolha do usuário.
        """
        print("""Olá, o que você deseja fazer:
              1- Salvar dados
              2- Recuperar dados
              3- Excluir dados""")
        i = int(input(": "))
        return i
    
    def insertdata(self):
        """Solicita ao usuário que insira dados e retorna as informações fornecidas.

        Returns:
            Tuple[str, int, int]: Nome, idade e CPF inseridos pelo usuário.
        """
        print("Ok, digite os dados!")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))
        return nome, idade, cpf
    
    def rescuedata(self):
        """Solicita ao usuário um CPF para buscar dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.
        """
        print("Ok, digite o CPF referente aos dados que devem ser buscados!")
        cpf = int(input(": "))
        return cpf
    
    def deletedata(self):
        """Solicita ao usuário um CPF para excluir dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.
        """
        print("Ok, digite o cpf referente ao dados a ser excluído!")
        cpf = int(input(": "))
        return cpf