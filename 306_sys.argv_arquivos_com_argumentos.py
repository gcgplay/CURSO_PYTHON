# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

# No terminal: python 306_sys.argsv "argumento_2" "argumento_3"
argumentos = sys.argv
qtd_argumentos = len(argumentos)

# print(qtd_argumentos) # 3

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')