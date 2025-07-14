#142 isinstace - para saber se objeto é de determinado tipo
# é instância de...
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    print(item, isinstance(item, set)) #verifica se o item é set (conjunto) - True
    
for item in lista:
    if isinstance(item, set): #verifica se é set
        print('SET')
        item.add(5) #adiciona no set
        print(item, isinstance(item, set)) #{0, 1, 5} True

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)