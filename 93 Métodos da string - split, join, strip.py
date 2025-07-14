"""
métodos da string
split e join com list e str
split - divide uma string (list)
strip - tira os espaços do começo e do fim da string (l - left| r - right)
join - une uma string
"""

#frase = 'Olha só que coisa interessante.'
#lista_palavras = frase.split() #divide em cada espaço
#print(lista_palavras) #['Olha', 'só', 'que', 'coisa', 'interessante.'


#frase = 'Olha só que, coisa interessante.'
#lista_frases = frase.split(',') #divide na vírgula
print(lista_frases) #['Olha só que', ' coisa interessante']

#editar a lista usando valores dela mesmo
#lista_frases = frase.split(',') #divide na vírgula
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) # Olha só que
			           # coisa interessante.

frase = '    Olha só que   , coisa interessante    '
for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip() 
print (lista frases) #['Olha só que', 'coisa interessante'] - lista sem espaços

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #cria uma nova lista e deixa salva a original com os espaços

# print(lista_frases_cruas)
# print(lista_frases)

frases unidas = '-'.join('abc')
print(frases_unidas) #a-b-c

frases_unidas = ', '.join(lista_frases)
print(frases_unidas) #Olha só que, coisa interessante.