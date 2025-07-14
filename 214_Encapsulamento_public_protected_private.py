# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       usado na classe e nas suas subclasses
#       não DEVE ser usado fora da classe
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

# Em Python não tem a essas restrições no sistema,
# cabe aos desenvolvedores respeitarem essas conversões
# conforme consta na PEP-8.

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private() #pode ser usado em qualquer lugar da classe
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
# print(f._protected) #funciona, mas não deve ser usado fora da classe
# print(f._metodo_protected()) #não deve ser usado fora da clase
# print(f._Foo__metodo_private()) #forma de acessar private, mas não deve ser usado
print(f.metodo_publico())