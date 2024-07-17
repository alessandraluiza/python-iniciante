class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

fabio = Funcionario('Fabio', 7000)
print(fabio.dados())

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()

fernando = (Admin('Fernando', 14000))
print(fernando.dados())

fernando.atualizar_dados('Fernandinho')
print(fernando.dados())