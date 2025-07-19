class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    def quem_sou(self):
        print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C): # HERANÇA MULTIPLA #chama na ordem passada
    ...

    # def quem_sou(self):
        # print('D')

d = D()
d.quem_sou() # D

# ao comentar o método em D, ele será buscado na próxima
# classe da ordem mro, no caso B a primeira passada como parâmetro
d.quem_sou() # B


# se não tivesse o método em B, ele buscaria no mais próximo
# que é a classe C passada como parâmetro
d.quem_sou() # C

# para verificar a ordem
print(D.__mro__)
print(D.mro())