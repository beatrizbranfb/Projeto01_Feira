from package.models.estoque import Estoque
class Carrinho:
    def __init__(self):
        self.produtos = {}

    def listar_carrinho(self):
        if not self.produtos:
            print("Carrinho vazio.")
        else:
            for produto in self.produtos:
                print(produto)

    def adicionar_produto(self, Estoque):
        Estoque.mostrar_estoque()
        nome = input("Qual produto deseja adicionar?: ").strip().title()
        quantidade = int(input(f"Quantas unidades de {nome} deseja adicionar?: "))
        if not nome in Estoque.frutas:
            print("Produto não disponível no estoque.")
            return
        else:
            if nome in self.produtos:
                print(input(f"Produto {nome} já está no carrinho. Deseja atualizar quantidade? (s/n): "))
                if input().lower() == 's':
                    self.produtos[nome].quantidade += quantidade
                    print(f"Quantidade de {nome} atualizada para {self.produtos[nome].quantidade}.")
                else:
                    return
            else:
                print(f"{nome} adicionado ao carrinho com {quantidade} unidades.")


    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print(f"{produto} removido do carrinho.")
        else:
            print(f"{produto} não está no carrinho.")


    def finalizar_pedido(self, estoque):
        if not self.produtos:
            print("Carrinho vazio!")
            return
    
        total = 0
        for nome, qtd in self.produtos.items():
            fruta = estoque.frutas[nome]
            total += fruta.preco * qtd 
            fruta.quantidade -= qtd  
    
        print(f"Total a pagar: R${total:.2f}")
        print("Pedido finalizado! Entregaremos em sua residência.")
        self.produtos.clear()