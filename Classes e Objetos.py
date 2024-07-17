jogador_loteria_1 = {
    'nome': 'Pedro',
    'numeros': (13, 4, 52, 23, 67, 82)
}

jogador_loteria_2 = {
    'nome': 'Pedro',
    'numeros': (13, 4, 52, 23, 67, 82)
}

print(jogador_loteria_1 == jogador_loteria_2)

#classe é um modelo ou uma representação de um objeto
#Objeto é uma instância de uma classe

class JogadorLoteria:
    def __init__(self):
        self.nome = 'Pedro'
        self.numeros = (13, 4, 52, 23, 67, 82)

    def total(self):
        return sum(self.numeros)

jogador_1 = JogadorLoteria()
jogador_2 = JogadorLoteria()
print(jogador_1.nome)
print(jogador_1.numeros)
print(jogador_1.total())

print(jogador_1 == jogador_2) #ambos agora são objetos e objetos são diferentes.







