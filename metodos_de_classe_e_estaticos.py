class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

    def applicar_aumento(self):
        self.salario = self.salario * self.aumento

fabio = Funcionario('Fabio', 7000)
fabio.applicar_aumento()
print(fabio.dados())
