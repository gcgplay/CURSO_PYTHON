from dataclasses import dataclass #decorator

@dataclass
# dataclass(init=False) # precisaria definir o init manualmente
class Pessoa:
    nome: str
    sobrenome: int

    def __post_init__(self): #precisa ter o init de dataclass
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def dados(self):
    #     return f'{self.nome} {self.idade}'

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    print(p1) #__repr__()
    print(p1.nome_completo)