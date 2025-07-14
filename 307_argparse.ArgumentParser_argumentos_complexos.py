# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser #definir quais argumentos o script 
                                    #aceitará pela linha de comando

parser = ArgumentParser() #Cria uma instância do parser.
                          #objeto que  vai configurar os argumentos 
                          #que seu script pode receber.

# parser.add_argument('-b') # chave
# args = parser.parse_args()
# print(args.b) # -b - ERRO - falta o valor do argumento
              # tem que passar um valor de b
              # -b 123

parser.add_argument(
    '-b', '--basic', #Define duas formas de passar o argumento: -b (forma curta) ou --basic (forma longa).
    help= 'Mostra "Olá mundo" na tela',
    type=str, #tipo do argumento
    metavar='STRING',
    default='Olá mundo', #valor padrão, caso não informe
    # required=True #obriga o usuário a passar o valor
    nargs='+' #para passar mais de um argumento - cria uma lista
    ) #irá pegar o argumento basic

# parser.add_argument(
#     '-v', '--verbose',
#     help= 'Mostra logs',
#     action = 'store_true' #retorna True se v for passado
#     )
# python nomedoarquivo.py -b "Atenção" -b "Basic" -b "Casa" -v

args = parser.parse_args() # lê os argumentos passados na linha de comando 
                           #e os armazena no objeto args
print(args.b)

# if args.b is None:
if args.basic is None:
    print('Você não passou o valor de b.')

else:
    # print('O valor de b: ', args.b)
    print('O valor de basic: ', args.basic) #-b 123

# para ver qual comando passar:
# python nomedoarquivo.py --help 
# nomedoarquivo.py [-h] [-b BASIC]
# BASIC - o que você quer passar

print(args.verbose)