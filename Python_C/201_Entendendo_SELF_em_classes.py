# self é uma convenção utilizada quando queremos
# referenciar a mesma instância
# Classe - Molde (geralmente sem dados)
# Instancia da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instância

class Carro:
    def __init__(self, nome):
    #def __init__(abc, nome):
    #def __init__(blabla, nome):
        #blabla.nome = nome
        #abc.nome = nome
        self.nome = nome

    def acelerar(self):
    #def acelerar(efg):
    #def acelerar(blabla):
        #print(f'{blabla.nome} está acelerando...')
        #print(f'{efg.nome} está acelerando...')
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
#Carro.acelerar() #ERRO - falta um argumento posicional - self
                 #você está acelerando o molde do biscoito

Carro.acelerar(fusca) #acelerar o fusca - FUNCIONA

fusca.acelerar() #CORRETO
                 #aqui seleciona o objeto em si que irá acelerar

celta = Carro('Celta')
celta.acelerar() #CORRETO
Carro.acelerar(celta) #FUNCIONA