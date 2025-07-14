#159 __init__.py para IMPORT e inicialização dos packages em Python
# https://stackoverflow.com/questions/2386714/why-is-import-bad

#criar o arquivo __init__.py dentro do package

#__init__.py no package
# print('Você importou o package', __name__)
# def dobra (x):
#     return x * 2

#se for feita a importação dos parâmetros dos modulos no __init__
#eles ficaram disponíveis como métodos de aula159_package. no MAIN
# from aula159_package.aula159_m import nova_variavel, variavel, soma_do_modulo

# nesse caso poderia fazer a importação * para importar tudo
# from aula159_package.aula159_m import *

#pode fazer o mesmo para o módulo m2
# from aula159_package.aula159_m2 import *

###**** F2 - altera o nome de um elemento em todos os locais que ele aparecer ****###
#----------------------------------------------------
#MAIN
#Enganar o Python, o __init__ faz o package se comportar como módulo
import aula159_package #Você importou o package aula159_package

print(aula159_package.dobra(2)) #4

#como tem o import dos parâmetros do módulo no __init__
#o aula159_package. terá todos esses parâmetros disponíveis
print(aula159_package.soma_do_modulo(2, 3))

#agora pode ser feita a importação direto no package também
from aula159_package import soma_do_modulo
print(soma_do_modulo(2, 3))