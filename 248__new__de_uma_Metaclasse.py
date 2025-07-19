
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type): #cria uma metaclasse
    def __new__(mcs, nome, bases, dct): #pode executar tarefas
                                        #antes da criação da classe
        print('METACLASS NEW')
        cls = super().__new__(mcs, nome, bases, dct)
        cls.atributo = 1234
        cls.__repr__ = meu_repr
        return cls

        if 'falar' not in cls.__dict__: #se falar não estiver definido
                                        #lança o erro
            raise NotImplementedError('Implemente falar')


# class Pessoa(object, metaclass=type): #padrão automático
class Pessoa(object, metaclass=Meta): #herda a meta classe criada
    
    #falar = 123 #burlar o if

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('Falando...')

p1 = Pessoa('Luiz')
print(p1.atributo)
print(p1)
print(p1.falar()) # se não estiver em def = ERRO
                  # not callable