# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação (qualquer coisa).
from abc import ABC, abstractmethod

#para ser abstrata precisa ter um método abstrato
#pensamento
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None #property - setter
        self.name = name 

    @property #método que se comporta como atributo
    def name(self):
        # return 123
        return self._name

    @name.setter
    @abstractmethod #deve vir mais interno
    def name(self, name): ...

#classe concreta
#fala seu pensamento
class Foo(AbstractFoo): 
    # name = '' #substituiria a property - atributo
    def __init__(self, name): #sobreposição
        super().__init__(name)
        # print('Sou inútil')

    # @name.setter #Erro - name não está definido, pois é da outra classe
    # def name(self, name):
    #     self._name = name

    # @AbstractFoo.name.setter - funciona
    # def name(self, name):
    #     self._name = name

foo = Foo('Bar')
print(foo.name) #chama getter