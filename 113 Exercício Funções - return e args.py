#113 Exercício Funções - return e args

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        
resultado = multiplicar(2, 4, 6)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

#def par_impar(numero):
    #if numero % 2 == 0:
        #return True
    #return False

# -- ou --

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
#retorno = par_impar(16)

#if retorno:
    #print('Esse número é PAR')
#else:
    #print('Esse número é IMPAR')
print(par_impar(16))
print(par_impar(5))