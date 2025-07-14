#111 *args - argumentos não nomeados (empacotamento e desempacotamento)
"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto) #1 2 [3 4]


# def soma(x, y):
#     return x + y

#def soma(*args):
    #print(args) #empacota a tupla passada

#soma(1, 2, 3, 4, 5, 6)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
#outra_soma = soma(numeros) #envia uma tupla para dentro de outra tupla
outra_soma = soma(*numeros) # * desempacotar
print(outra_soma)

print(sum(numeros)) #função que já faz a soma dos números
# print(*numeros)