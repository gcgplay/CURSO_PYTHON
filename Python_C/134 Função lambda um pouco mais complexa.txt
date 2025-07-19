134 Função lambda um pouco mais complexa

def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y

#def = lambda
#print
#    executa(
#        lambda x, y: x + y
#    )
#    executa(soma, 2, 3) #mesma coisa
#    soma(2, 3) # mesm coisa
#)

# -- ou poderia atribuir a funcao lambda a uma variável
soma = executa(
    lambda x, y: x + y,
    2, 3 #valores
)
print(soma)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


#duplica = cria_multiplicador(2) - mesma coisa abaixo
duplica = executa(
    lambda m: lambda n: n * m, #lambda = def -> função : função
                               #função que recebe parâmetro m e retorna
                               #uma função que recebe n e retorna n * m
    4 #define n = 4 
)
print(duplica(2)) #chama a função passando o valor de m

#lambda passando args
#print(
#    executa(
#        lambda *args: sum(args), #faz a soma de todos os números passados
#        1, 2, 3, 4, 5, 6, 7
#    )
#)