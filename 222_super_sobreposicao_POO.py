# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa): 
        super().__init__(atributo) #chama A e passa o atributo para A
        self.outra_coisa = outra_coisa # atributo de B
                                       # que também será atributo de C

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.') #pode executar comandos antes do init
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super(C, self).metodo()  # Eu sou o C, a partir de mim procure o próximo método (self)
                                   # Pela ordem de prioridade método = B = super
        # super(B, self).metodo()  # Eu sou B, a partir de B procure o próximo método 
                                   # Puxa o método de A que se torna o primeiro método a se executado
        # super(A, self).metodo()  # object
        A.metodo(self) #mesma coisa de super - A
        B.metodo(self) # B
        print('C')


# print(C.mro()) #retorna o method resolution order
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo() # A se super(B, self)
           # B se super(C, self)
# print(c.atributo_a) #C terá os atributos da classe A e B
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo() 