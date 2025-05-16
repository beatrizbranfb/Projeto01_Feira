class Fruta:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome}: {self.quantidade} unidades"