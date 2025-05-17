from package.controllers.serialobjson import DataRecord
from package.models.estoque import Estoque
from time import sleep

class TelaAdm:
    def __init__(self):
        self.clientes = DataRecord("database_clientes.json")
        self.produtos = DataRecord("database_produtos.json")
        self.estoque = Estoque()

def menu(self):
    while True:
        print("\n=== MENU DO ADMINISTRADOR ===")
        print("1. Listar clientes")
        print("2. Listar produtos")
        print("3. Confirmar entrega para um cliente")
        print("4. Acessar estoque")
        print("5. Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            self.listar_clientes()
        elif escolha == "2":
            self.listar_produtos()
        elif escolha == "3":
            Estoque.menu()
        elif escolha == "4":
            self.estoque.adicionar_produto()
        elif escolha == "5":
            print("Saindo da área do administrador...")
            break
        else:
            print("Opção inválida.")
