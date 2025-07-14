#118 Exercício Closure e funções que retornam outra função

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2) #cria uma função multiplicar com multiplicador 2
triplicar = criar_multiplicador(3) #cria uma função multiplicar com multiplicador 3
quadruplicar = criar_multiplicador(4) #cria uma função multiplicar com multiplicador 4

print(duplicar(2)) #imprime o retorno de uma função multiplicar com multiplicador 2 e numero 2
print(triplicar(2)) #imprime o retorno de uma função multiplicar com multiplicador 3 e numero 2
print(quadruplicar(2)) #imprime o retorno de uma função multiplicar com multiplicador 4 e numero 2