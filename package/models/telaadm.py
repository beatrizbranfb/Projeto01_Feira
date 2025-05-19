from package.controllers.serialobjson import DataRecord
from package.models.produtos.estoque import Estoque
from time import sleep

class TelaAdm:
    def __init__(self, estoque: Estoque):
        self.clientes = DataRecord("package/controllers/db/database_clientes.json")
        self.produtos = DataRecord("package/controllers/db/database_produtos.json") 
        self.estoque = estoque

    def menu(self):
        while True:
            print("\n=== MENU DO ADMINISTRADOR ===")
            print("1. Listar clientes")
            print("2. Acessar estoque")
            print("3. Confirmar entrega para um cliente")
            print("4. Sair")

            escolha = input("Escolha: ")

            if escolha == "1":
                self.listar_clientes()
            elif escolha == "2":
                self.estoque.menu()
            elif escolha == "3":
                self.confirmar_entrega()
            elif escolha == "4":
                print("Saindo da área do administrador...")
                break
            else:
                print("Opção inválida.")


    def listar_clientes(self):
        print("\n=== LISTA DE CLIENTES ===")
        clientes = self.clientes.read()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for i, cliente in enumerate(clientes):
                print(f"{i + 1}. Nome: {cliente['nome']}")
        
    
    def confirmar_entrega(self):
        print("\n=== CONFIRMAR ENTREGA ===")
        nome = input("Nome do cliente que deseja confirmar entrega: ").strip().title()
        clientes = self.clientes.read()
        for i, cliente in enumerate(clientes):
            if cliente['nome'] == nome:
                print(f"Entrega confirmada para {nome}!")
                del clientes[i]
                self.clientes.overwrite(clientes) 
                return
        print("Cliente não encontrado.")