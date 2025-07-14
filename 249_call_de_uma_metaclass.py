# Problema = não conseguir ver coisa que estão dentro da instância
# o call vai ser responsavel por criar a instancia e chamar o init
# quando se define um def __call__, quer dizer que a instância da classe
# se torna executável
# quando se faz um call na metaclass está tratando dos parenteses 
# da chamada da classe
l

def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs) #criar a instancia dentro do call

        print(instancia.__dict__)
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia


class Pessoa(metaclass=Meta):
    # falar = 123

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        # self.nome = nome #se esquecer de definir nome
                           #ERRO será informado pelo if do call

    def falar(self):
        print('FALANDO...')


p1 = Pessoa('Luiz') #tratado pelo call
p1.falar()