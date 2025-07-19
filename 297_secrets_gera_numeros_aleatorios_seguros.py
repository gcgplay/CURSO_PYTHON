import secrets
import string as s
from secrets import SystemRandom as Sr

#GERAR UMA SENHA SEGURA
# letras + numeros + pontuações
#cria uma senha aleatória juntando 12 caracteres
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))


#torna o módulo random seguro - para senhas e criptografia
#REALMENTE ALEATÓRIO
random = secrets.SystemRandom 

# seed
#   -> NÃO FAZ NADA
random.seed(10)

print(secrets.randbelow(100)) #numero aleatorio abaixo do valor
print(secrets.choice([10, 11, 12])) #escolher um dos elementos

#EXECUTA OS MESMO COMANDO DE RANDOM, MAS DE FORMA SEGURA
#SEM INTERFERÊNCIA DO SEED
r_range = random.randrange(10, 20, 2)
print(r_range)

r_int = random.randint(10, 20)
print(r_int)

r_uniform = random.uniform(10, 20)
print(r_uniform)


nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

print(random.choice(nomes))