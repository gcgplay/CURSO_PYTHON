def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora foi executada')

        def aninhada(*args, **kwargs):
            print('Recebeu os parâmetros, ', a, b, c)
            print('Aninhada')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funcoes


#@decoradora() #se colocar os parênteses ele tenta executa o decorador
              #mas precisa passar a função no argumento
#@passa_parametros (1, 2, 3) #funciona dando acesso ao parâmetros para a decoradora
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

#decoradora = fabrica_de_decoradores() #None, None, None
#multiplica = decoradora(lambda x, y: x * y)
multiplica = fabrica_de_decoradores()(lambda x, y: x * y)


dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)