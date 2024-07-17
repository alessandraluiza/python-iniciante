#if -> Se
#else -> Se não
devo_continuar = True
if devo_continuar:
    print("Continue")

pessoas_conhecidas = ['João', 'Maria', 'Joana', 'Fabio']
pessoa = input ("Entre com o nome de uma pessoa:")

if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")

if pessoa not in pessoas_conhecidas:
    print("Você não conhece essa pessoa")

if pessoa in pessoas_conhecidas:
    print("Você conhece essa pessoa")
else:
    print("Você não conhece essa pessoa")

if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa))
else:
    print("Você não conhece {}".format(pessoa))

pessoa = 4

if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(pessoa))
else:
    print("Você não conhece "+str(pessoa))
