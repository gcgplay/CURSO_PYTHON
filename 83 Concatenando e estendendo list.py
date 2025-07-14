83 Concatenando e estendendo list

"""
extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b #junta as listas em uma
lista_a.extend(lista_b) #adiciona a lista_b na lista_a

print(lista_a)
