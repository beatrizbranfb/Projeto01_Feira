from package.models.pessoas.pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, nome, login, senha):
        super().__init__(nome)
        self.login = "login123"
        self.senha = "senha321"

    def __str__(self):
        return f"Nome: {self.nome} Login: {self.login} Senha: {self.senha}"
    

    
