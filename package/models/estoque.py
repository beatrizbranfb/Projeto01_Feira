from package.models.frutas import Fruta  

class Estoque:
    def __init__(self):
        self.frutas = {}

    def adicionar_fruta(self):
        nome = input("Qual o nome da fruta que deseja adicionar? ").strip().title()
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            print("Quantidade inválida! Use números positivos.")
        return

        if nome in self.frutas:
            self.frutas[nome].quantidade += quantidade
            print(f"Quantidade de {nome} atualizada para {self.frutas[nome].quantidade}.")
        else:
            self.frutas[nome] = Fruta(nome, quantidade)
            print(f"{nome} adicionada ao estoque com {quantidade} unidades.")
            preco = float(input("Qual o preço da fruta?: "))
            self.frutas[nome].preco = preco
            print(f"Preço de {nome} definido como R$ {preco:.2f} cada.")

    def mostrar_estoque(self):
        if not self.frutas:
            print("Estoque vazio.")
        else:
            print("\n--- ESTOQUE ATUAL ---")
            for fruta in self.frutas.values():
                print(fruta)

    def menu(self):
        while True:
            print("\n--- ESTOQUE ---")
            print("1. Adicionar Fruta")
            print("2. Ver Estoque")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_fruta()
            elif opcao == "2":
                self.mostrar_estoque()
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")