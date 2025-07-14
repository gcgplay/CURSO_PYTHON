81 alterando uma lista com índices - append, del, pop

"""
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]

# lista[2] = 300 #altera o valor do elemento do índice 2 da lista
# numero = lista[2] #atribui o valor do índice 2 da lista à variável numero

# del lista[2] #apaga o elemento no índice 2 da lista, reorganiza a lista 
# ao deletar um elemento o Python reorganiza todos os elementos da lista, evite fazer alterações desse tipo
# em listas muito grandes utiliza muito processamento
# em listas deve-se inserir e retirar elementos do final dela

# print(lista)
# print(lista[2])
lista.append(50) #adiciona no final da lista
lista.pop() #remove o último elemento da lista e retorna esse valor
ultimo_valor = lista.pop(3) #salva o valor removido 
print(lista, 'Removido,', ultimo_valor)