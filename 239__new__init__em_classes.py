# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

# Similar a construtores de outras linguagens
# método que cria objetos

# new - pouco utilizado - não recebe self - cria a instância

#class A:
class A(object):

    def __new__(cls): #cria a instância/objeto
    # def __new__(cls, x):
    # def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois de criar a instância')
        instancia.x = 123
        #return super().__new__(cls)
        return instancia

    def __init__(self):
    # def __init__(self, x): # se acrescenta um parâmetro, acrescenta tbm no new
        # self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'

a = A() # o que o Python faz, abaixo:
# a = object.__new__(A)
# a.__init__() #retorna um novo objeto
print(A)
print(a.x) #123