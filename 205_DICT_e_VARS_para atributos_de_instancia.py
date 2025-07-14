#eles mantêm um objeto do tipo mapping
#dicionário/atributo que mantem os valores que podem ser escritos
#dentro desse objeto

class Pessoa:
    
    ano_atual = 2022 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
       

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 35)
# dados = {'nome': 'João', 'idade': 35}
# p1 = Pessoa(**dados)

# p1.nome = 'EITA'
# print(p1.nome)
# del p1.nome
# print(p1.idade)
# pode-se manipular os atributos
# o __dict__ retém os valores dos atributos
# o vars também apresenta um dict

print(p1.__dict__) #{'nome': 'João', 'idade': 35}
print(vars(p1)) #{'nome': 'João', 'idade': '35}

# manipula atributos de um objeto
p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'EITA'
print(p1.__dict__) #{'nome': 'EITA', 'idade': 35, 'outra': 'coisa'}
print(vars(p1))
print(p1.outra) #coisa
