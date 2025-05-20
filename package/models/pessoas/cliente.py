#Herança: Classe filho de pessoa
from package.models.pessoas.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, contato, residencia):
        super().__init__(nome)
        self.contato = contato
        self.residencia = residencia

    def __str__(self):
        return f"Nome: {self.nome}, Contato: {self.contato}, Residência: {self.residencia}"
