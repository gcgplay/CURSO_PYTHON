class Animal:
    nome = 'Leão'

# print(nome) # não é possível acessar diretamente algo
              #que está declarado no escopo da classe

print(Animal.nome) # dessa forma é possível pegar a variável
                   #dentro da classe sem instanciar essa classe

class Carro:
    def __init__(self, nome):
        self.nome = nome # da instância da classe

        variavel = 'valor' # Essa variável só é acessivel dentro 
                           # do escopo de init
        print(variavel)

    def acao(self):
        #print(variavel) #ERRO - não definida no escopo desse método
        return f'{self.nome} está executando uma ação' # acessivel na instância da classe

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}' #alimento precisa ser passado na chamada do método
# print(Animal.nome) #ERRO - o nome agora é para a instância
# É necessário criar um objeto (instância) da classe para
# acessar nome no print
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.acao())
print(leao.comendo('carne'))
