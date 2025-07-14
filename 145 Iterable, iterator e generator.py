#145 Iterable, iterator e generator

import sys
#iterável - item sequencial em que se pode acessar os valores sequecialmente
#iterator - entregar um valor por vez, sabe apenas o próximo valor

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()
print(next(iterator)) #Eu
print(next(iterator)) #Tenho
print(next(iterator)) #__iter__
#print(next(iterator)) #ERRO - StopIteration

#generator - funções que sabem pausar
#          -todo generator é um iterator, mas iterator não é generator
#          -se você não quer uma grande quantidade de dados salvo na memória -> generator

lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista)) #lista enorme salva na memória - tamanho 87616
print(sys.getsizeof(generator)) #local da memória - tamanho 112

#o generator fica esperando chamar um elemento por vez
print(next(generator))
print(next(generator))

for n in generator:
    print(n) #não tem tamanho
             #não tem índice
             #sabe apenas o próximo item sequecialmente
             #pausa a cada execução (next)