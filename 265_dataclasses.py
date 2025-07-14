# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass #decorator

#é uma classe normal
#maneira facilitada de criar uma classe já com todos os métodos
@dataclass
class Pessoa:
    nome: str
    idade: int

    #pode definir métodos
    def dados(self):
        return f'{self.nome} {self.idade}'

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    print(p1) #__repr__()
    print(p1 == p2) #__eq__()
    print(p1.dados())