87 Desempacotamento e introdução a tuplas

nome1, nome2 = ['Maria', 'Helena', 'Luiz'] #ValueError - tem menos variáveis que valores para serem atribuídos

nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz'] #ValueError - não tem valor para ser atribuído à variável nome4

-- CORRETO - mesma quantidade de valores e variáveis --
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print (nome2)

-- Ou faz-se o empacotamento --
# nome1, *resto = ['Maria', 'Helena', 'Luiz']

# -- utiliza-se o _ para indica que uma variável não será utilizada em nenhum outra parte do código --
_, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome) #Helena

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz'] # resto pega o restante da variável mesmo que vazio
print(nome, resto) #Luiz []