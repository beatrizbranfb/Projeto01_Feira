from package.models.produtos.estoque import Estoque
from package.models.pessoas.cliente import Cliente
from package.controllers.serialobjson import DataRecord
from package.models.produtos.frutas import Fruta
from time import sleep

class TelaCliente:
    def __init__(self):
        self.produtos = {}
        self.clientes_db = DataRecord("package/controllers/db/database_clientes.json")
        self.cliente = None
        self.estoque = Estoque()

    def dados(self):
        nome = input("Qual o seu nome?: ")  
        contato = input("Qual o seu número para contato?: ")
        residencia = input("Qual o seu endereço?: ")

        self.cliente = {
            'nome': nome,
            'contato': contato,
            'residencia': residencia,
            'pedidos': []
        }

        self.clientes_db.write(self.cliente)
        return self.cliente

    
    def menu(self):
        while True:
            print("\n--- Menu Carrinho ---")
            print("1 - Listar produtos")
            print("2 - Adicionar produto ao carrinho")
            print("3 - Remover produto do carrinho")
            print("4 - Finalizar pedido")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.estoque.mostrar_estoque()
            elif opcao == "2":    
                self.adicionar_produto()
            elif opcao == "3":
                produto = input("Qual produto deseja remover?: ").strip().title()
                self.remover_produto(produto)
            elif opcao == "4":
                self.finalizar_pedido()
            elif opcao == "5":
                print("Saindo do carrinho...")
                break
            else:
                print("Opção inválida.")


    def adicionar_produto(self):
        self.estoque.mostrar_estoque()
        nome = input("Qual produto deseja adicionar?: ").strip().title()
  
        if nome not in self.estoque.frutas:  
            print("Produto não disponível no estoque.")
            return

        try:
            quantidade = int(input(f"Quantas unidades de {nome} deseja adicionar?: "))
            if quantidade <= 0:
                print("Quantidade deve ser positiva!")
                return
                
            if self.estoque.frutas[nome].quantidade < quantidade:
                print(f"Estoque insuficiente. Disponível: {self.estoque.frutas[nome].quantidade}")
                return

            if nome in self.produtos:
                self.produtos[nome] += quantidade
                print(f"Quantidade de {nome} atualizada para {self.produtos[nome]}.")
            else:
                self.produtos[nome] = quantidade
                print(f"{nome} adicionado ao carrinho com {quantidade} unidades.")

        except ValueError:
            print("Quantidade inválida!")
            return
        
    def remover_produto(self, produto):
        if produto in self.produtos:
            del self.produtos[produto]
            print(f"{produto} removido do carrinho.")
        else:
            print(f"{produto} não está no carrinho.")


    def finalizar_pedido(self):
        if not self.produtos:
            print("Carrinho vazio!")
            return

        total = 0
        pedido = []
            
        for nome, qtd in self.produtos.items():
            fruta = self.estoque.frutas.get(nome)
            if not fruta:
                print(f"Produto {nome} não encontrado no estoque.")
                continue
                    
            if fruta.quantidade < qtd:
                print(f"Estoque insuficiente para {nome}. Disponível: {fruta.quantidade}, solicitado: {qtd}.")
                continue

            total += fruta.preco * qtd
            fruta.quantidade -= qtd  
            pedido.append({"produto": nome, "quantidade": qtd})

            if pedido:
                self.cliente["pedidos"].extend(pedido)
                self.clientes_db.write(self.cliente)
                print(f"\nTotal a pagar: R${total:.2f}")
                print("Pedido finalizado! Entregaremos em sua residência.")
                self.produtos.clear()