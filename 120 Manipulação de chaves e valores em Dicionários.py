#120 Manipulação de chaves e valores em dicionários
pessoa = {}

##
##

#pessoa['nome'] = 'Luiz Otávio'
#print(pessoa)

chave = 'nome' #define dinamicamente apenas o nome da chave

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome'] #APAGAR chave
print(pessoa)
#print(pessoa['sobrenome']) #ERRO - chave sobrenome foi apagada
print(pessoa['nome'])

# print(pessoa.get('sobrenome')) #NONE quando a chave não existe
if pessoa.get('sobrenome') is None:
    print('CHAVE NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')