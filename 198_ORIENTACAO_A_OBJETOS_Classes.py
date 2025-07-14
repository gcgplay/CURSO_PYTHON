# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes. PRIMEIRA LETRA MAIUSCULA
# string = 'Luiz' # a classe str gera o objeto 'Luiz'
                  #Luiz é instancia de str
# print(string.upper())
# print(isinstance(string, str))

#class IniciaLetraMaiuscula:
#    ...

class Pessoa:
    #atributos - dados
    # def métodos()
    def __init__(self, nome, sobrenome):
        self.nome = nome #p1.nome
        self.sobrenome = sobrenome #p1.sobrenome
        


p1 = Pessoa('Luiz', 'Otávio') #gerar um novo(a) objeto/instancia da classe
# p1.nome = 'Luiz' #atributo nome
# p1.sobrenome = 'Otávio' #atributo sobrenome

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome) #para acessar um atributo
print(p1.sobrenome) #para acessar um atributo

print(p2.nome)
print(p2.sobrenome)