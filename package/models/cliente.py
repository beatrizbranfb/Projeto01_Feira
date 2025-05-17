from package.models.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, contato, residencia):
        super().__init__(nome)
        self.contato = contato
        self.residencia = residencia

    def __str__(self):
        return f"Nome: {self.nome}, Contato: {self.contato}, Residência: {self.residencia}, Compras: {self.compras}"
    
    def add_cliente(self):
        self.nome = input("Qual o seu nome?: ")  
        self.contato = input("Qual o seu número para contato?: ")
        self.residencia = input("Qual o seu endereço?: ")
        return {'nome': self.nome, 'contato': self.contato, 'residencia': self.residencia}