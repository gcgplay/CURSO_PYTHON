#Introdução ao try/except
"""
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
#---
#print(1234)
#print(4567)
#int('a') #ERRO - ValueError

#---
numero_str = input('Vou dobrar o número que você digitar: ') #sempre retorna uma string
# numero_float = float(numero) #precisa converter a entrada

try: #tenta executar o código, se ocorrer algum erro vai para o except
    numero_float = float(numero_str) #se o usuário digitar uma letra, não é possível converte = ERRO
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')