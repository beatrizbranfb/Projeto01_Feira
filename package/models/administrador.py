from package.models.pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, nome, login, senha):
        self.login = "login123"
        self.senha = "senha321"
        super().__init__(nome)

    def __str__(self):
        return f"Nome: {self.nome} Login: {self.login} Senha: {self.senha}"
    

    
