# Exercício - Adiando execução de funções

#O código abaixo está com erro
#soma() missing 1 required positional argument: 'y'
#O valor do parâmetro y não foi passado para a função
# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 5) #ERRO - está precipitando a execução
                                         #da função soma, antes de passar 5
# multiplica_por_dez = criar_funcao(multiplica, 10)

# --- Solução --- 

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# closure
# cria uma NOVA função baseada na função soma
# com o parâmetro x definido
# mas que precisa receber o valor do parâmetro y para ser executada
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10)) #fechamento do closure, passando o último parâmetro
print(multiplica_por_dez(10))