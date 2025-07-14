133 NIntrodução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) #ordena a lista original, com ordem invertida
# sorted(lista) #cria uma cópia rasa ordenada da lista
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#para ordenar uma lista de dicionários é necessário passar as instruções de ordenação para o Python
#por meio de uma função
#def ordena(item):
#    print(item)
#    return item['nome'] #passa a chave que será usada para a ordenação

#lista.sort(key=ordena) #Ordena a impressão dos dicionários de acordo com a chave nome

# -- ou usando lambda --
lista.sort(key=lambda item: item['nome']) #faz o mesmo que função ordena, em uma linha
                                          #ordena a lista original
#print('------------------')
print(lista)

# -- ou por sorted - cópia rasa ordenada --
sorted(lista, key=lambda item:item['nome'])


#def exibir(lista): #imprime item por item da lista desejada
    #for item in lista:
        #print(item)
    #print()

#l1 = sorted(lista, key=lambda item: item['nome']) #coloca a cópia da lista ordenada em uma variável
#l2 = sorted(lista, key=lambda item: item['sobrenome'])

#exibir(l1) #chama a função que exibe
#exibir(l2)