#140.4 Revisão Lista Comprehension - fatiamento (agrupamento)

string = 'Gabriel Carmo'
nova_string = [letra for letra in string] #gera uma lista de letra por letra
#nova_string = ''.join([letra for letra in string]) #junta a string novamente

#fatiamento (grupos)
numero_de_letras = 2 #agrupa de 2 em 2 caracteres, permite escolher o tamanho do agrupamento
nova_string = [
    string[indice:indice + numero_de_letras] #pega o indice atual até dois caracteres adiante
    for indice in range(0, len(string), numero_de_letras) #cria uma sequencia de indices pulando de 2 em 2
]

print(nova_string)