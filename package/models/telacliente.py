from package.models.produtos.estoque import Estoque
from package.models.pessoas.cliente import Cliente
from package.controllers.serialobjson import DataRecord

class TelaCliente:
    def __init__(self, estoque: Estoque):
        self.estoque = estoque
        self.produtos = {}
        self.db = DataRecord("package/controllers/db/database_clientes.json")
        self.produtos_db = DataRecord("package/controllers/db/database_produtos.json")
        self.cliente = None

    def dados(self):
        nome = input("Qual o seu nome?: ").strip().title()
        contato = input("Qual o seu número para contato?: ")
        residencia = input("Qual o seu endereço?: ")
        self.cliente = Cliente(nome, contato, residencia)
        self.db.add(self.cliente.__dict__)

    def menu(self):
        self.dados()
        while True:
            print("\n--- CARRINHO ---")
            print("1. Listar produtos")
            print("2. Adicionar produto ao carrinho")
            print("3. Remover produto do carrinho")
            print("4. Finalizar pedido")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_carrinho()
            elif opcao == "2":
                self.adicionar_produto()
            elif opcao == "3":
                produto = input("Produto a remover: ").strip().title()
                self.remover_produto(produto)
            elif opcao == "4":
                self.finalizar_pedido()
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

    def listar_carrinho(self):
        if not self.produtos:
            print("Carrinho vazio.")
        else:
            print("\n--- CARRINHO ---")
            for nome, qtd in self.produtos.items():
                print(f"{nome} - {qtd} unidade(s)")

    def adicionar_produto(self):
        self.estoque.mostrar_estoque()
        nome = input("Produto a adicionar: ").strip().title()
        if nome not in self.estoque.frutas:
            print("Produto não disponível.")
            return
        try:
            qtd = int(input(f"Quantas unidades de {nome} deseja? "))
            if qtd <= 0 or qtd > self.estoque.frutas[nome].quantidade:
                print("Quantidade inválida ou fora do estoque.")
                return
            self.produtos[nome] = self.produtos.get(nome, 0) + qtd
            print(f"{nome} adicionado ao carrinho.")
        except ValueError:
            print("Insira uma quantidade válida.")

    def remover_produto(self, produto):
        if produto in self.produtos:
            del self.produtos[produto]
            print(f"{produto} removido.")
        else:
            print("Produto não encontrado no carrinho.")

    def finalizar_pedido(self):
        if not self.produtos:
            print("Carrinho vazio.")
            return

        if not hasattr(self, "cliente"):
            print("Cliente não identificado. Por favor, preencha os dados primeiro.")
            return

        total = 0
        pedido_items = []

        for nome, qtd in self.produtos.items():
            fruta = self.estoque.frutas[nome]
            total += fruta.preco * qtd
            fruta.quantidade -= qtd
            pedido_items.append({
                "nome": nome,
                "quantidade": qtd,
                "preco_unitario": fruta.preco,
                "subtotal": fruta.preco * qtd
            })

        novo_pedido = {
            "itens": pedido_items,
            "total": total
        }

        clientes = self.db.get_all() 
        for cliente in clientes:
            if cliente["nome"] == self.cliente.nome and cliente["contato"] == self.cliente.contato:
                cliente.setdefault("pedidos", []).append(novo_pedido)
                break

        self.db.overwrite(clientes) 
        produtos_atualizados = [fruta.__dict__ for fruta in self.estoque.frutas.values()]
        self.produtos_db.overwrite(produtos_atualizados)

        print(f"Total: R$ {total:.2f}")
        print("Pedido finalizado e enviado para entrega!")
        self.produtos.clear()
