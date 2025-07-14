#140.5 Revisão Lista Comprehension - lower, uper, title e flat
nomes = ['gabriel', 'josé', 'maria']
novos_nomes = [nome.title() for nome in nomes] #cria uma nova lista, coloca a primeira letra maiuscula
#como colocar apenas a última maiuscula?
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
    ]
print(novos_nomes)

#Flat - organizar todos os elementos em uma única lista
numeros = [[numero, numero ** 2] for numero in range(10)]
print (numeros)
# [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

flat = [y for x in numeros for y in x] #x é cada sublista de números
                                       #y é cada elemento individual das sublistas
print(flat)
#[0, 0, 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, 6, 36, 7, 49, 8, 64, 9, 81]