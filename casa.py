class Casa:
    def __init__(self, tamanho, altura, cor):
        print('Construindo casa')
        self.tamanho = tamanho
        self.altura = altura
        self.cor = cor

    def imprimir(self):
        print(f'Tamanho: {self.tamanho}, \nAltura: {self.altura}, \nCor: {self.cor}')

    def calcularArea(self):
        print(f'Essa casa vai ter um pé direito com {self.altura}')
        print(f'De area construida sera de {self.tamanho * self.altura}')


class Apartamento:
    def __init__(self, tamanho, altura, cor):
        print('Construindo apartamento')
        self.tamanho = tamanho
        self.altura = altura
        self.cor = cor

    def imprimir(self):
        print(f'Tamanho: {self.tamanho}, \nAltura: {self.altura}, \nCor: {self.cor}')

    def calcularArea(self):
        print(f'Esse apartamento vai ter um pé direito com {self.altura}')
        print(f'De area construida sera de {self.tamanho * self.altura}')
