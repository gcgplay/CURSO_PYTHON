class Multiplicar: #multiplicar não recebe argumentos
    # def __init__(self, args): #Multiplicar não é callable
    # def __init__(self, func):
    def __init__(self, multiplicador):
        # print('INIT', args) #INIT <function soma>
        # self.func = func
        self._multiplicador = multiplicador

    # def __call__(self, *args, **kwds): #torna Multiplicar executável
    def __call__(self, func): 
        # print(args, kwds) # (2, 2)
        def interna(*args, **kwds):
            resultado = func(*args, **kwds)
            return resultado * self._multiplicador
        # return resultado #classe decoradora que também
        return interna                                        #executa a ação de multiplicar
        # return self.func(*args, **kwds) #repassa os argumentos para func

# o decorador será passado agora com letra inicial MAIUSCULA
# para indicar que é uma classe que está decorando o método soma
# @Multiplicar
@Multiplicar(10) # executaria o init da classe aqui - mudaria tudo, pede argumento
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2)
print(dois_mais_dois)


class Multiplicar: 
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwds):
            resultado = func(*args, **kwds)
            return resultado * self._multiplicador
        return interna

@Multiplicar(10)
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2)
print(dois_mais_dois)