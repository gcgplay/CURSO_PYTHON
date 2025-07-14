123 Métodos em dicionários (pop, get, popitem, update)

# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe')) #retorna o valor, None ou algo especificado

# nome = p1.pop('nome') #retorna o valor e apaga do dicionário
# print(nome)
# print(p1)
# ultima_chave = p1.popitem() #retorna o valor da última chave e apaga ela
# print(ultima_chave)
# print(p1)

#atualiza o dicionário
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30) #passando argumentos nomeados
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista) #passando iterável com chave e valor para atualizar o dict
print(p1)