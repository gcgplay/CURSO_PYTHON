# Variáveis são usadas para salvar algo na memória do computador.
# PEP8 (guia de estilos do código Python)
# -> inicie variáveis com letras minúsculas, pode usar números e underline _.
# O sinal de = é o operador de atribuição. 
# Ele é usado para atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

#recebe qualquer valor literal de tipos imutáveis e primitivos (str, int, bool, float)
# nome_completo = 'Luiz Otávio Miranda'
# soma_dois_mais_dois = 2 + 2 #pode passar uma expressão na variável => Literal[4]
# print(int('1'), type(int('1')))
# int_um = bool('1') nome errado, pois teria que ser int_um = int('1')
# print(int_um, type(int_um)) #mesmo comando com variável
# print(nome_completo, soma_dois_mais_dois)

#variáveis não são usadas para abreviar código

nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18 #expressão com variável dentro de outra variável - bool
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)