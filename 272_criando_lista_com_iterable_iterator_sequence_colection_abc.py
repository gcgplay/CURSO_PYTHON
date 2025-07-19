# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

# Iteratos - objeto diferente - métodos mágicos - collection

from collections.abc import Iterable #precisa existir __iter__
from collections.abc import Sequence

#class MyList():
#class MyList(Iterator): #precisa do método __next__
class MyList(Sequence): #precisa de __getitem__, __setitem__, __len__
    def __init__(self):
        self._data = {} #dicionario - chave/valor
        self._index = 0
        self._next_index = 0 #__next__

    def append(self, *values): #método para adicionar valores (*sobrenome)
        for value in values:
            self._data[self._index] = value
            self._index += 1 #adicionar o item no próximo indice do dicionário
                             #senão iria alterar o mesmo índice

    def __len__(self) -> int:
        return self._index #tamanho da lista

    def __getitem__(self, index): #chama o item com []
        return self._data[index] #valor de um indice

    def __setitem__(self, index, value): #atribui ao []
        self._data[index] = value

    def __iter__(self):
        return self #retorna a própria classe

    def __next__(self): #for
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index] 
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista._data) #protegido
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista: #não é realizado pelo next se o index não for zerado
        print(item)
    print('---')