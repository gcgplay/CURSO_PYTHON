# Desempacotamento em chamadas de métodos e funções



lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

a, b, c = lista #Erro - sobra elementos
a, b, c, *_ = lista
print (a, c) # Maria 1



# primeiro, b, *_, antipenultimo, ultimo = lista
# print(p, u, ap) # Maria Eduarda 3

# for nome in lista:
#     print (nome, end=' ') #imprime a lista em uma linha

#É o mesmo que:
# print(*lista) # Maria Helena 1 2 3 Eduarda

string = 'ABCD'
print(*string) # A B C D

tupla = 'Python', 'é', 'legal'
print(*tupla) # Python é legal

# lista dentro de lista
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
print(*salas, sep='\n') #exibe cada lista em uma linha