from dataclasses import dataclass, asdict, astuple #converte a clase para dict ou tupla

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__== '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys()) #chaves
    print(asdict(p1).values()) #valores
    print(asdict(p1).items()) #chaves, valores
    print(astuple(p1)[0]) #nome
    