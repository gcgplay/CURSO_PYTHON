75 for usando continue, break, else, etc

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break #else não será executado

    for j in range(1, 3):
        print(i, j)
else: #se concluir o for será executado
    print('For completo com sucesso!')