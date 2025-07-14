94 Listas dentro de listas (iteráveis dentro de iteráveis)

#lista de listas
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

# print(salas[1]) # ['Elaine']
# print(salas[1][0]) # Elaine
# print(salas[0][1]) # Helena
# print(salas[2][2]) # Eduarda
# print(salas[2][3][3]) # 30

for sala in salas: #exibe cada sala
    print(f'A sala é {sala}')
    for aluno in sala: #exibe cada aluno
        print(aluno)