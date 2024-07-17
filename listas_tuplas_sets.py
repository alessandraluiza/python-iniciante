nota_1 = 3
nota_2 = 5
nota_3 = 6
nota_4 = 4
nota_5 = 8

print((nota_1+nota_2+nota_3+nota_4+nota_5)/5)

notas = [3,5,6,4,8]
print(notas)

notas.append(5)
print(notas)

print(len(notas))#quantidade de elementos

print(sum(notas)) #soma dos elementos

print(sum(notas)/len(notas))

print(notas[0])

#Tuplas

tupla = (3,4,5)
tupla += (4,)
print(tupla)

tupla = tupla + (7,)
print(tupla)

#Sets

set_nota = {1,2,3,4,5,5,3,5}
print(set_nota)

set_nota.add(7)
print(set_nota)

set_nota.add(1)
print(set_nota)

set_nota.add("Valor")
print(set_nota)
