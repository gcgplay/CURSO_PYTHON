132 Ex Lista de lista e set (achar duplicado)
"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

#(2)função para encontrar o primeiro duplicados
def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set() #vazio
    primeiro_duplicado = -1 #retorno padrão caso não tenha numeros duplicados
    
    for numero in lista_de_inteiros: #(3)verifica número por número de cada lista
        #print(numero) #imprime número por número de cada lista
        if numero in numeros_checados: #se o número já estiver em números numeros_checados
            primeiro_duplicado = numero #então ele será o primeiro_duplicado
            break #se achou o primeiro_duplicado, pode parar o programa
        numeros_checados.add(numero) #senão o número é adicionado a numeros_checados pela primeira vez 
        
    return primeiro_duplicado #se parou no break retorna o valor do primeiro_duplicado, senão -1

for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista)) #(1) aqui chama a função passando lista por lista da 
                                                     #lista_de_listas_de_inteiros