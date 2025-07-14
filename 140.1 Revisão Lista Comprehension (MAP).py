140.1 Revisão Lista Comprehension (MAP)

def divisãoFn(x, y):
    return x / y

def multiplicaçãoFn(x, y):
    return x * y

def potenciaçãoFn(x, y)
    return x ** y

numeros = [1, 2, 3, 4, 5]

#novos_numeros = numeros #apenas aponta para o mesmo local da memória
                        #se alterar algo em uma altera a outra também
#novos_numeros = numeros.copy() #cópia rasa

#pega um iterável e gera outro iterável (map)
novos_numeros = [numero for numero in numeros] #cria uma nova Lista
                                               #para cada numero em numeros adiciona o numero na variavel numero da lista novos_numeros
#mesma coisa que acima
novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero)
    
# divisao = [numero / 2 for numero in numeros] #cria uma nova lista  
#                                              #com cada numero de numeros dividido por 2
#                                              #[0.5, 1, 1.5, 2.0, 2.5]
#                                              #sem alterar a lista original (map)
# multiplicação = [numero * 2 for numero in numeros]
# quadrado = [numero ** 2 for numero in numeros] #jogar em funções que podem ser reutizadas - cima

divisão = [divisãoFn(numero, 2) for numero in numeros] 
multiplicação = [multiplicaçãoFn(numero, 2) for numero in numeros]
quadrado = [potenciaçãoFn(numero, 2) for numero in numeros]

print(numeros)
print(divisão)
print(multiplicação)
print(quadrado)