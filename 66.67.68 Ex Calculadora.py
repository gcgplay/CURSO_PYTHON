66.67.68 - Ex Calculadora

""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True #flag para verifica se a conversão float ocorreu
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue #volta para o início

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos: #verificar se o operador digitado é válido
        print('Operador inválido.')
        continue

    if len(operador) > 1: #verifica se foi digitado mais de um operador
        print('Digite apenas um operador.')
        continue

    # OPERAÇÕES
    if operador == '+':
	print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
	print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
	print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    elif operador == '/':
	print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    else:
	print('Não deveria chegar aqui.')


    sair = input('Quer sair? [s]im: ').lower().startswith('s') #converte para minusculas e primeira letra s

    if sair is True:
        break