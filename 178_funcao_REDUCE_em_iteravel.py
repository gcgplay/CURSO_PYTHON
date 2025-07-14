#REDUZIR O ITERÁVEL A UM ÚNICO VALOR

from functools import reduce
 
produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
 
# como a reduce funciona
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']
 
 
total = reduce(
    lambda ac, p: ac + p['preco'], #total (acumulador)
    produtos,
    0 #valor inicial
)
 
print('Total é', total)
 
#Tudo a mesma coisa abaixo:
 
# total = 0
# for p in produtos:
#     total += p['preco']
 
# print(total)

#-------------------
#total = '' 
# print(sum([p['preco'] for p in produtos]))