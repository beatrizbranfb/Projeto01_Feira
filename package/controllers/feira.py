from package.controllers.serialobjson import DataRecord
from package.models.cliente import Cliente
from package.models.administrador import Administrador
from package.models.telaadm import TelaAdm
from time import sleep

class Feira:
    def __init__(self):
        self.__clientes = DataRecord("package/controllers/db/database_clientes.json")
        self.__administradores = DataRecord("package/controllers/db/database_administradores.json")
        self.sair = False
        self.opcoes = {
            "1": self.__area_administradores,
            "2": self.__area_cliente,
            "3": self.sair_do_sistema
        }

    def menu(self):
        while True:
            escolha = input("Escolha o que deseja:\n1. Sou administrador\n2. Sou cliente\n3. Sair\nEscolha: ")
            acao = self.opcoes.get(escolha)
            if acao:
                if not acao():  
                    break
            else:
                print("Opção inválida!")

    def sair_do_sistema(self):
        print("Saindo do sistema...")
        sleep(2)
        return False  

    def __area_administradores(self):
        print("--- BEM-VINDO ADMINISTRADOR ---")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        adm = Administrador("admin", login, senha)
        if adm.login == login and adm.senha == senha:
            print("Login realizado com sucesso!")
            sleep(1)
            tela_adm = TelaAdm()
            tela_adm.menu()
        else:
            print("Login ou senha incorretos!")
        return True

    def __area_cliente(self):
        print("\n--- ÁREA DO CLIENTE ---")
        Cliente.add_cliente(self)
        return True
