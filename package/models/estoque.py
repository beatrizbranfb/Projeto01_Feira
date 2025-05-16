from package.models.frutas import Fruta  

class Estoque:
    def __init__(self):
        self.frutas = {}

    def adicionar_fruta(self):
        nome = input("Qual o nome da fruta que deseja adicionar? ").strip().title()
        quantidade = int(input(f"Quantas unidades de {nome} deseja adicionar? "))

        if nome in self.frutas:
            self.frutas[nome].quantidade += quantidade
            print(f"Quantidade de {nome} atualizada para {self.frutas[nome].quantidade}.")
        else:
            self.frutas[nome] = Fruta(nome, quantidade)
            print(f"{nome} adicionada ao estoque com {quantidade} unidades.")

    def mostrar_estoque(self):
        if not self.frutas:
            print("Estoque vazio.")
        else:
            print("\n--- ESTOQUE ATUAL ---")
            for fruta in self.frutas.values():
                print(fruta)

    def  menu(self):
        while True:
            print("\n--- ESTOQUE ---")
            print("1. Adicionar Fruta")
            print("2. Ver Estoque")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                Estoque.adicionar_fruta(self)
            elif opcao == "2":
                Estoque.mostrar_estoque(self)
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")