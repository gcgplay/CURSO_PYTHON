88 Tuplas - listas imutáveis

# mais rápida que a list
# quando não precisa alterar

# -- declaração de uma tupla --
nomes = 'Maria', 'Helena', 'Luiz'
# -- ou --
nomes = ('Maria', 'Helena', 'Luiz')

# -- converter uma list em tupla --
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
nomes = list(nomes)

print(nomes[-1]) #índices igual a list