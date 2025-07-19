# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #pode se executado direto na classe
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod #pode se executado direto na classe, não tem self
                 #factory method - cria um novo objeto ou alguma coisa
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50) #Pessoa (nome, 50)

    @classmethod 
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade) #Pessoa ('Anônima', idade)

#método sem nenhuma instância, chamado direto na classe
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(20)
print(Pessoa.ano)
Pessoa.metodo_de_classe()
