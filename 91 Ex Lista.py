"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True: #loop infinito, programa não para
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ') #começar colocando as opções

# INSERIR
    if opcao == 'i': #inserir item (append)
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor) #insere e volta para inicio


#APAGAR
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ') #input gera str

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.') #quando digitar algo diferente de número
        except IndexError:
            print('Índice não existe na lista') #quando digitar número diferente dos índices
        except Exception:
            print('Erro desconhecido')

#LISTAR
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')