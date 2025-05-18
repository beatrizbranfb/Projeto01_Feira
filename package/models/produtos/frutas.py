class Fruta:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: {self.quantidade} unidades : R$ {self.preco:.2f} cada"

    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }

    @staticmethod
    def from_dict(dados):
        return Fruta(dados["nome"], dados["quantidade"], dados["preco"])
