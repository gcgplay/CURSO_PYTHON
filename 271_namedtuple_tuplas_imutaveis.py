# namedtuples - tuplas IMUTÁVEIS com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# classe para atributos, sem métodos, apenas registro de dados
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm

# from collections import namedtuple #para criar um objeto do tipo
from typing import NamedTuple #para criar uma classe


class Carta(NamedTuple): #parecido com a dataclass
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

#valores padrão
# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
as_espadas = Carta('A', 'ESPADAS')

print(as_espadas._asdict()) #dicionário da namedtuple
print(as_espadas) # Carta(valor='A', naipe='ESPADAS')
print(as_espadas[0]) #A
print(as_espadas.valor) #A
print(as_espadas[1]) # ESPADAS
print(as_espadas.naipe) # ESPADAS

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)


for valor in as_espadas:
    print(valor)