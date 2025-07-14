# 149.150 try e except para tratar exceções
# a = 18
# b = 0
# c = a / b #erro

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000]) #IndexError
    c = a / b #ZeroDivisionError
    print('Linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Mensagem:', error)
    print('Nome/Tipo:', error.__class__.__name__)
except Exception: #trata qualquer erro
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')