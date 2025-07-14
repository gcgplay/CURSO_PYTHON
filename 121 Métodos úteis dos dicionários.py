# 121 Métodos úteis dos dicionários em Python
# len - quantas chaves tem no dicionário
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0) #adiciona uma chave e valor se ela NÃO existir no dicionário
print(pessoa['idade']) 
# print(len(pessoa)) #3
# print(list(pessoa.keys())) #['nome', 'sobrenome']
# print(list(pessoa.values()))
# print(list(pessoa.items()))

#for chave in pessoa.keys():
    #print(chave) #chaves
    
# for valor in pessoa.values():
#     print(valor) #valores

# for chave, valor in pessoa.items():
#     print(chave, valor) #separados