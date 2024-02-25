class Screen:
    """Classe responsável por interagir com o usuário.

    Esta classe fornece métodos para exibir telas de opções e coletar dados
    inseridos pelo usuário relacionados a operações de salvar, recuperar e excluir dados.

    Methods:
        main_screen(): Exibe a tela principal e obtém a escolha do usuário.

        Returns:
            int: Escolha do usuário.

        save_data(): Solicita ao usuário que insira dados a serem salvos e retorna as informações fornecidas.

        Returns:
            Tuple[str, int, int]: Nome, idade e CPF inseridos pelo usuário.

        get_data(): Solicita ao usuário um CPF para buscar dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.

        delete_data(): Solicita ao usuário um CPF para excluir dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.
    """

    def main_screen(self):
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

    def save_data(self):
        """Solicita ao usuário que insira dados a serem salvos e retorna as informações fornecidas.

        Returns:
            Tuple[str, int, int]: Nome, idade e CPF inseridos pelo usuário.
        """
        print("Ok, entre com os dados a serem salvos!")
        nome = input("Nome:")
        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))
        return nome, idade, cpf
    
    def get_data(self):
        """Solicita ao usuário um CPF para buscar dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.
        """
        print("Ok, entre com o cpf referente ao dado a ser recuperado!")
        cpf = int(input(": "))
        return cpf
    
    def delete_data(self):
        """Solicita ao usuário um CPF para excluir dados e retorna o valor inserido.

        Returns:
            int: CPF inserido pelo usuário.
        """
        print("Ok, digite o cpf referente ao dado a ser excluído!")
        cpf = int(input(": "))
        return cpf
