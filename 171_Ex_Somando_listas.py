"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [] #lista que vai receber os resultados

tamanho_menor_lista = min(len(lista_a), len(lista_b))

for i in range(tamanho_menor_lista):
    lista_soma.append(lista_a[i] + lista_b[i]) #adiciona o resultado da soma de cada item da lista na lista_soma
print(lista_soma)

# -- ou --
# sabendo que a lista menor é lista_b

lista_soma = []

for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# -- ou --
#com list comprehension + zip

lista_soma = [x + y for x, y in zip(lista_a, lista_b)] #pega o x na lista_a e o y na lista_b indice por indice
                                                       #(1, 1) (2, 2) (3, 3) (4, 4)
                                                       #e retorna a soma dos elementos de cada índice