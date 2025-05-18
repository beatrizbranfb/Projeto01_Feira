from package.controllers.serialobjson import DataRecord
from package.models.produtos.estoque import Estoque
from time import sleep

class TelaAdm:
    def __init__(self, estoque):
        self.estoque = estoque
        self.clientes = DataRecord("database_clientes.json")
        self.produtos = DataRecord("database_produtos.json")
        self.estoque = Estoque()

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
                sleep(2)
                return True
    
    def confirmar_entrega(self):
        print("\n=== CONFIRMAR ENTREGA ===")
        clientes = self.clientes.read()
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        for i, cliente in enumerate(clientes):
            print(f"{i + 1}. Nome: {cliente['nome']}")

        try:
            escolha = int(input("Escolha o número do cliente para confirmar a entrega: ")) - 1
            if 0 <= escolha < len(clientes):
                cliente_confirmado = clientes.pop(escolha)  
                print(f"Entrega confirmada para {cliente_confirmado['nome']}.")
                self.clientes.write(clientes)

            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")
