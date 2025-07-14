#110 Retorno de valores das funções (return)
"""
Retorno de valores das funções (return)
"""
#variavel = print('Luiz') #ao executar retorna Luiz
                          #print exibe algo na tela, não é return
#print(variavel) #retorna None

#-------------------
#def soma(x, y):
#    ...

#variavel = soma(1, 2)
#print(variavel) #None

#-----------------------
def soma(x, y):
    if x > 10:
        return [10, 20] #se if = True, encarra a função aqui
    #else:
    return x + y 
    # retorna um valor que pode ser usado em outro local


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2) #se não tivesse return = ERRO
soma2 = soma(3, 3) 
print(soma1) #4
print(soma2) #6
print(soma(11, 55)) #[10, 20]