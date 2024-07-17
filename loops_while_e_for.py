minha_variavel = "ola mundo"
print(len(minha_variavel))

print(minha_variavel[0])
print(minha_variavel[1])
print(minha_variavel[2])

# for -> para
# while -> enquanto

for letra in minha_variavel:
    print(letra)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# range(start, stop, step)
# start = 0
# step = 1
print(range(10))

print(list(range(11)))

print(set(range(10)))

print(tuple(range(10)))

print(list(range(1, 12, 2)))

numeros_pares = list(range(0, 11, 2))
print(numeros_pares)

for numero in numeros_pares:
    print(numero ** 3)

#while -> enquanto
x = 0
while x < 10:
    print(x ** 3)
    x = x + 2 #incrementar

usuario_quiser = True
while usuario_quiser == True:
    usuario_input = input("Quer continuar ? (S/N) ")
    if usuario_input == 'N':
        usuario_quiser = False
