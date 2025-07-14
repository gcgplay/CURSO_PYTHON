#Tipos built-in, documentação, tipo imutável, métodos de string

"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: str, int, float, bool - objetos - podem ser executadas ações (métodos)
"""

string = 'Luiz Otávio'
#string[3] = 'ABC' #não pode ser feito, pois é imutável

# para fazer a alteração é preciso criar outra variável
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)

#métodos de string
string = '1000'
print(string.zfill(10)) #adiciona zeros a esquerda