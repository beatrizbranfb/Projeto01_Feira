class Fruta:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: {self.quantidade} unidades : R$ {self.preco:.2f} cada"