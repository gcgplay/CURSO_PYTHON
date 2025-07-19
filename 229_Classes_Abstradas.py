# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod


class Log(ABC): #NÃO PODEM ser instânciadas diretamente
                #herda de ABC - metaclass=ABCMeta)
    @abstractmethod
    def _log(self, msg): ... #método abstrato - forçar outras classes
                             # a criarem métodos concretos

    def log_error(self, msg): #método concreto
        return self._log(f'Error: {msg}')

    def log_success(self, msg): #método concreto
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log): #herda Log
    def _log(self, msg): #implementa método abstrato log
        print(f'{msg} ({self.__class__.__name__})')


# l = Log() #antes de adicionar @abstractmethod,
            #não gera erro, é abstrata, mas não tem 
            #métodos abstratos

# l = Log() #com o decorator @abstracmethod a classe se
            #torna completamente abstrata, log não pode ser
            #usada diretamente, pois é uma classe contrato
            #Erro - não posso instanciar a classe abstrata log

l = LogPrintMixin()
l.log_error('Oi')