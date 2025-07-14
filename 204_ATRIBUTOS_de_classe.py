# Atributos de classe
class Pessoa:
    #atributo = 'valor'
    ano_atual = 2022 #atributo de classe, disponível para todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        #self.ano_atual = 100

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        #return self.ano_atual - self.idade #busca primeiro na instância
                                            #depois busca na classe


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual) #é possível acessar o atributo pela classe
# Pessoa.ano_atual = 1 #altera o atributo para todas as instâncias

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())