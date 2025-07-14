class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade - idade

@property #decorador que permite transformar um método 
          #de uma classe em uma propriedade
def nome(self):
    return self._nome

@nome.setter
def nome(self, nome: str):
    self._nome = nome

@property
def idade(self):
    return self._idade
    
@idade.setter
def idade(self, idade: int):
    self._idade = idade

def __repr__(self): #De Pessoa
    class_name = type(self).__name__
    attrs = f'({self.nome!r}, {self.idade!r})'
    return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

if __name__ == '__main__':
    import contas
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1) #precisa do repr
    print(c1.conta)
