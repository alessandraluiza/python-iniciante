print([x ** 2 for x in range (5)])

print([x + 10 for x in range (5)])

print(list(range (0,10,2)))

print(10 % 3) #resto

print(1 % 2)

print([n for n in range(11) if n % 2 == 0]) #números pares

print([n for n in range(11) if n % 2 == 1]) #números impares

pessoas = ['Ana ', 'manuela', 'FELIPe ', 'PedrO']
ana = ' Ana'
print (ana)

print(ana.strip()) #retira espaços
print(ana.lower()) #todas letras minusculas
print(ana.upper()) #todas letras maiusculas
print(ana.capitalize()) #primeiro caracter maiusculo
print(ana.strip().capitalize())


pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]
print(pessoas_normalizadas)


