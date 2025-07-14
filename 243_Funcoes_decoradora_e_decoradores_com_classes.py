#Função decoradora com classes
#Funções Decoradoras: Funções que modificam o comportamento de outras funções ou classes.
#criar um método dentro da classe usando uma função
def adiciona_repr(cls): #função de recebe uma classe
    def meu_repr(self): #função que recebe self, como se estivesse dentro da classe
                        #assim a função será atrelada ao __repr__
                        #chamado dentro da outra função
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr #Substitui o método __repr__ da classe pela função meu_repr.
    return cls #retorna a mesma classe decorada
    

class MyReprMixin: #Mixins: Classes que fornecem métodos para serem usados por outras classes.
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

# class SuperTime:
#     ...

@adiciona_repr #Aplica a função decoradora adiciona_repr à classe Time, 
	       #adicionando o método __repr__ definido na função decoradora.
class Time:
# class Time(SuperTime, MyReprMixin):
    def __init__(self, nome):
        self.nome = nome

    # passado para classe MyReprMixin
    # def __repr__(self): 
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr

@adiciona_repr #Aplica a função decoradora adiciona_repr à classe Time, 
	       #adicionando o método __repr__ definido na função decoradora.
class Planeta:
# class Planeta(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome

# @adiciona_repr
# Time = adiciona_repr(Time) # funciona para transforma a impressão em repr
                             # sobrescreve a definição da classe
brasil = Time('Brasil') #sem o método repr imprime apenas o local da memória
portugal = Time('Portugal') 

# @adiciona_repr
# Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

# Time({'nome': 'Brasil'})
# Time({'nome': 'Portugal'})
# Planeta({'nome': 'Terra'})
# Planeta({'nome': 'Marte'})