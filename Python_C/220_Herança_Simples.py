# todas as classes em Python já herdam a classe 
# builtins object

# class Foo(object):
#     ...


# help(Foo) # Q - para sair

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__) #nome, sobrenome, nome classe


class Cliente(Pessoa): # todo o código que está em Pessoa está acessível em Cliente
    def falar_nome_classe(self): # executa esse método que está dentro da classe
                                 # nem chega a buscar o método na classe Pessoa 
                                 # devido ao Method Resolution Order
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__) 


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio') # já adiciona nome e sobrenome, herdados de Pessoa
c1.falar_nome_classe() # aqui o método vem de dentro da própria classe
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe() # nesse caso ele busca o método em Pessoa
print(a1.cpf)
# help(Cliente) # mostra informações sobre a classe
                # mostra a ordem em que os dados são buscados nas classes
                # procura em Cliente, depois em Pessoa

# Ordem de Solução --> Cliente --> Pessoa --> object