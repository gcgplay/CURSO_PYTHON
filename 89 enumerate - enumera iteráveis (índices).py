89 enumerate - enumera iteráveis (índices)


# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')] - cria uma tupla
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

#lista enumera = list(enumerate(lista)) #converte o enumerate para list
#print(lista enumerada) #dessa forma imprime os índices/itens

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# for item in lista_enumerada:
#     print(item)

#após o print acima o iterator foi consumido, não terá mais nada em lista_enumerada

#para corrigir, para os valores não esgotarem, deve-se sempre chamar um novo iterator (enumerate)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# é possível separar os dois valores
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# -- ou --
#for índice, nome in enumerate(lista):
#     print(índice, nome)

#imprimir item por item das tuplas
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')