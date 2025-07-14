82 Alterando list (del, clear, extend) e inserindo itens

"""
    insert - inserir em determinado índice
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1] #apaga o último item da lista
# lista.clear() #limpa a lista
lista.insert(100, 5) #faz a inserção, mas no último índice, não no 100
print(lista[10]) #ERRO - IndexError - fora do range