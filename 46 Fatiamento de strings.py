"""
Fatiamento de strings

-Indices-
012345678
Olá mundo
987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:]) #pega do caracter do índice 4 até o final - mundo
print(variavel[4:7]) #pega do caracter do indice 4 até o caracter do indice 6, o indice final indicado é omitido - mun
print(variavel[:5]) #Olá m
print(variavel[-8:-2]) #lá mun
print(variavel[3]) #espaço
print(len(variavel)) #tamanho da string - 9
print(variavel[0:9:1]) #imprime os caracteres do indice 1 ao 8 pulando de 1 em 1
print(variavel[::-1]) #inverte a string
