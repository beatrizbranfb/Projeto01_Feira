from package.models.telaadm import TelaAdm
from package.models.telacliente import TelaCliente
from package.models.pessoas.administrador import Administrador
from package.models.produtos.estoque import Estoque
from time import sleep

class Feira:
    def __init__(self):
        self.estoque = Estoque()
        self.adm = TelaAdm(self.estoque)
        self.cliente = TelaCliente(self.estoque)
        self.admin = Administrador("Admin", "login123", "senha321")

    def menu(self):
        while True:
            print("\n----------FEIRA----------")
            print("1. Área do Administrador")
            print("2. Área do Cliente")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                if self.__login_admin():
                    self.adm.menu()
                else:
                    print("Login ou senha incorretos.")
            elif opcao == "2":
                print("Bem-vindo à área do cliente!")
                self.cliente.menu()
            elif opcao == "3":
                print("Encerrando sistema...")
                sleep(2)
                break
            else:
                print("Opção inválida.")

    def __login_admin(self): #encapsulamento privado pois não é utilizado apenas nessa classe
        login = input("Digite o login do administrador: ")
        senha = input("Digite a senha do administrador: ")
        return login == self.admin.login and senha == self.admin.senha    