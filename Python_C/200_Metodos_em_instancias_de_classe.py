#criar comportamentos dentro da classe (método)

#self é o mesmo que o objeto fora da classe - eu mesmo

class Carro:
    #def __init__(self): #sempre retorna None
    #def __init__(self, alguma_coisa='Sei lá'):
    def __init__(self, nome):
        self.nome = nome
        #self.nome = 'Fusca' #hard coded

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

#fusca = Carro() #declarando um nome direto na classe
                 #todos os Carros teriam o mesmo nome
fusca = Carro('Fusca')
#fusca.nome = 'Fusca'
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()