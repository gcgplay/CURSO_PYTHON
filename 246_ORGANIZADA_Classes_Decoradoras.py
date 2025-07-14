#Código 1
class Multiplicar: 
    def __init__(self, func): #Recebe uma função (func) como argumento
        self.func = func
        self._multiplicador = 10 #define um multiplicador fixo

    def __call__(self, *args, **kwds): #Permite que a instância da classe 
                                       #seja chamada como uma função.
        resultado = self.func(*args, **kwds) #Recebe os argumentos da função original, 
                                             #calcula o resultado
        return resultado * self._multiplicador #multiplica pelo valor do multiplicador.

@Multiplicar # Aplica a classe Multiplicar como decorador à função soma.
             # soma será substituída por uma instância de Multiplicar 
             # que encapsula a função original.
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2) # soma(2, 2) chama o método __call__ da instância de Multiplicar, 
                            # que calcula 2 + 2 e multiplica o resultado por 10.
print(dois_mais_dois)

#Código 2
class Multiplicar: 
    def __init__(self, multiplicador): #Recebe um valor de multiplicador (multiplicador) 
                                       #como argumento e o armazena.
        self._multiplicador = multiplicador

    def __call__(self, func): #recebe uma função (func) como argumento  
        def interna(*args, **kwds): # define uma função interna (interna)
            resultado = func(*args, **kwds) #calcula o resultado da função original
            return resultado * self._multiplicador #multiplica pelo valor do multiplicador.
        return interna #Retorna a função interna decorada.

@Multiplicar(10) #Aplica a classe Multiplicar como decorador à função soma, 
                 #passando o valor 10 como multiplicador.
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2) #chama a função interna decorada, 
                            #que calcula 2 + 2 e multiplica o resultado por 10.
print(dois_mais_dois)

# Diferenças de Implementação
# Passagem de Argumentos:

# Código 1: A classe Multiplicar recebe a função diretamente no método __init__.
# Código 2: A classe Multiplicar recebe o multiplicador no método __init__ e a função no método __call__.
# Estrutura do Decorador:

# Código 1: A instância da classe Multiplicar substitui diretamente a função decorada.
# Código 2: A instância da classe Multiplicar retorna uma função interna decorada que encapsula a função original.
# Flexibilidade:

# Código 1: O multiplicador é fixo (10) e não pode ser alterado sem modificar a classe.
# Código 2: O multiplicador é passado como argumento ao decorador, permitindo maior flexibilidade.