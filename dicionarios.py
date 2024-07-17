meu_set = {4, "valor",3,"qualquer"}
print(meu_set)

meu_dicionario = {'nome': 'Ana', 'idade':80}
print(meu_dicionario['nome'])

print(meu_dicionario['idade'])

minha_list_dic = [{'nome': 'Ana', 'idade':80}, {'nome': 'Jose', 'idade':45}, {'nome': 'Maria', 'idade':10}]
print(minha_list_dic[0])
print(minha_list_dic[1])
print(minha_list_dic[2])

print(minha_list_dic[1]['nome'])
print(minha_list_dic[1]['idade'])

loteria = {'nome': 'Fulano', 'numeros': (13,4,53,67,82)}
print(loteria['numeros'])

universidades = [
    {
        'nome': 'Universidade Federal do Rio de Janeiro',
        'sigla': 'UFRJ'
    },
    {
        'nome': 'Universidade de São Paulo',
        'sigla': 'USP'
    }
]
print(universidades)

print(loteria)
print(loteria['numeros'])
print(sum(loteria['numeros']))

loteria['nome'] = 'Ana'
print(loteria)







