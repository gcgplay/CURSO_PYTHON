# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
import time
# Funções:
# seed - baseado nos microsegundo do horário
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(time.time()) - aleatório
# random.seed(0) - nada mais é aleatório

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2) #entre 10 e 20, de 2 em 2
# print(r_range) #um número

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform) #float

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (NÃO repete)
novos_nomes = random.sample(nomes, k=3) #pega 3 elementos aleatórios de nomes
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (REPETE valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))