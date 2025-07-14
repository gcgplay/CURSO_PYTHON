#140.3 Revisão Lista Comprehension (Linhas e Colunas)

# for x in range(10): #linhas
#     for y in range(5): #colunas
#         print(x, y)

linhas_e_colunas = [
    (x, y) #parâmetros que serão gerados
    if y != 2 else (x, y * 100) #quando y = 2, multiplica y * 100
    for x in range(10)
    for y in range(5)
    if x != 2 #filtra tirando linha = 2
]
print(linhas_e_colunas)