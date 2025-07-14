#Exercício 1 - Revisão

"""Faça um programa que peça ao usuário para digitar um número inteiro, informe se o número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro."""

#--- Minha resolução ---

numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if (numero_int % 2 == 0):
        print(f'O numero {numero_int} é par.')
    else:
        print(f'O numero {numero_int} é impar.')
except:
    print('Você não digitou um número inteiro.')

#--- Resolução professor ---

entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

