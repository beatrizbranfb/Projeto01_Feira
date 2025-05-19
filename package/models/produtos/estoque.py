from package.models.produtos.frutas import Fruta
from package.controllers.serialobjson import DataRecord

class Estoque:
    def __init__(self):
        self.db = DataRecord("package/controllers/db/database_produtos.json")
        self.frutas = {}
        self.__carregar_frutas()

    def __carregar_frutas(self):
        dados = self.db.read()
        if dados:
            for f in dados:
                fruta = Fruta(f['nome'], f['quantidade'], f['preco'])
                self.frutas[fruta.nome] = fruta

    def adicionar_fruta(self):
        nome = input("Qual o nome da fruta que deseja adicionar? ").strip().title()

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            print("Quantidade inválida! Use números positivos.")
            return

        try:
            preco = float(input("Qual o preço da fruta?: "))
            if preco <= 0:
                raise ValueError
        except ValueError:
            print("Preço inválido! Use números positivos.")
            return

        if nome in self.frutas:
            self.frutas[nome].quantidade += quantidade
            self.frutas[nome].preco = preco  
            print(f"Quantidade de {nome} atualizada para {self.frutas[nome].quantidade}.")
        else:
            self.frutas[nome] = Fruta(nome, quantidade, preco)
            print(f"{nome} adicionada ao estoque com {quantidade} unidades e preço R$ {preco:.2f}.")

        dados = [{
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        } for f in self.frutas.values()]
        self.db.overwrite(dados)

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

