class Cliente():
    def __init__(self, nome, contato, residencia):
        self.nome = nome
        self.contato = contato
        self.residencia = residencia

    def __str__(self):
        return f"Nome: {self.nome}, Contato: {self.contato}, Residência: {self.residencia}"
