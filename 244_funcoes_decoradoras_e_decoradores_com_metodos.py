# Decorar um método

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

#função decoradora
def meu_planeta(metodo): #recebe um método
    def interno(self, *args, **kwargs): # Define um método interno 
                                        # que chama o método original (metodo) 
                                        # e modifica seu resultado.
        # resultado = self.falar_nome() - erro de recursão - chama o método dentro dele mesmo
        resultado = metodo(self, *args, **kwargs) 

        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr #Aplica a função decoradora adiciona_repr à classe Time,
               # adicionando o método __repr__ definido na função decoradora.
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta # Aplica a função decoradora meu_planeta 
                 # ao método falar_nome, modificando seu comportamento.
    def falar_nome(self): # o python substitui esse método pelo que foi retornado
                          # na função decoradora
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())