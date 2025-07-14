# Tudo que está em A está em B e C
# Mas o metodo é sobreposto
class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b' # herda o atributo_a e tem atributo_b
    def metodo(self):  # usa apenas o método dentro da classe
                       # o método com mesmo nome
        print('B')

class C(B):
    atributo_c = 'valor c' # herda o atributo_a e o atributo_b e tem atributo_c
    def metodo(self): # acessa apenas o método de C
        print('C')

c = C() # executa apenas C
print(c.atributo_a) #valor a
print(c.atributo_b) #valor b
print(c.atributo_c) #valor c
# C tem acesso a todos os atributos