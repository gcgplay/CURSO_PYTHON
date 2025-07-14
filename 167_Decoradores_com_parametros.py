def decoradora(func):
    print('Decoradora foi executada') #(2) decora a função soma
                                      #soma se torna função aninhada

    def aninhada(*args, **kwargs):
        print('Executou a aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora # (1) ao executar o código a função soma é passada para a função decoradora
def soma(x, y): 
    return x + y

dez_mais_cinco = soma(10, 5) #(3) quando a função soma for chamada com os parâmetros
                             # irá executar a função aninhada
print(dez_mais_cinco) #(4) imprime o res da função aninhada


#-------------------------------------------
# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
 
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes
 
 
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y
 
 
decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
 
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)