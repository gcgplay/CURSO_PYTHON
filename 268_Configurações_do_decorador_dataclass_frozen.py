from dataclasses import dataclass

# @dataclasses(frozen=True) #passar as configurações
                          #frozen congela a dataclass - 
                          #não pode definir ou atribuir nada nela

# @dataclass(repr=False, order=False) #sem repr - imprime local da memoria
                                      #sem order - não ordena

@dataclass #já importa todas as configurações
#SEMPRE É MELHOR VOCÊ GERAR UMA NOVA COISA DO QUE ALTERAR UMA COISA EXISTENTE
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    # p1 = Pessoa('Gabriel', 'Carmo')
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    
    # ordenadas = sorted(lista, reverse=True)
    ordenadas = sorted(lista, reverse=False, key=lambda p: p.nome)
    # ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome) #sobrenome

    #print(p1)
    print(ordenadas)