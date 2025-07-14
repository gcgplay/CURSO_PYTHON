# 141 Dictionary Comprehension (chave, valor) e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for chave, valor in produto.items():
    print(chave, valor)
    
dc = {
    chave: valor.upper() #método para string
    if isinstance(valor, str) else valor #verifica se o valor é str e faz o método upper, senão retorna valor
    for chave, valor
    in produto.items()
    if chave != 'categoria' #filter - somente a chave categoria
}

lista = [
    ('a', 'valor a'), #chave, valor
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
#ou dict(lista)

s1 = {2 ** i for i in range(10)} #dicionário de valores quadrados
print(s1)