from src.controller import Controller

#OBS:Atualize o local do banco de dados de acordo com os seus documentos!
bd_path = "Python/Projetos/MongoDb-e-SQLITE/SQLITE3/src/SQl/banco.db"

def main():
    """Função principal para iniciar o controlador e interagir com o usuário.

    Cria uma instância do controlador, inicia o controlador e continua até o usuário optar por sair.
    """
    controller_instance = Controller(bd_path)
    start = controller_instance.start_controller()

    while start:
        start = controller_instance.start_controller()
    
    del controller_instance

if __name__ == "__main__":
    main()