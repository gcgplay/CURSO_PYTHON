#157 Introdução aos package - importações no main

#criar um arquivo na raiz aula157.py (main)
#criar uma pasta aula157_package
#criar um arquivo módulo aula157_m dentro da pasta aula157_package
#criar outro módulo aula157_m2 dentro da mesma pasta aula157_package

#MAIN
# from sys import path
 
# import aula157_package.aula157_m
# from aula157_package import aula157_m
# from aula157_package.aula157_m import *
# # from aula99_package.modulo import soma_do_modulo

# # print(*path, sep='\n') #pastas do Python
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel) #ERRO, não está no __all__ do módulo

#o primeiro arquivo executado é o MAIN
print(__name__)

#comando Terminal
# ls | grep aula99
# aula99.py e aula99_package são irmãos

#criar mais um modulo no aula99_package => aula157_m2
from aula99_package.aula157_m import soma_do_modulo #do ponto de vista do MAIN
                                                    #caso não seja passado o caminho inteiro dentro do módulo 1
                                                    #ocorre um erro, pois dentro do aula157_m
                                                    #tem a import do aula157_m2
                                                    #como ele não está na mesma raiz do main
                                                    #ocorre ModuleNotFound

#Então todas as importações do programa inteiro, precisam ser relacionadas com o seu MAIN
from aula99_package.aula157_m import fala_oi, soma_do_modulo
#passando o caminho inteiro do package e módulo será possível acessar o m2 pela importação do m1

fala_oi() #vindo do m2, passado no m1, para ser usado aqui no MAIN

#---------------
#aula157_m.py
from aula157_m2 import fala_oi #importa o outro módulo
                               #se executar deste módulo irá funcionar
                               #pois estão no mesmo package
                               #mas não funcionaria o main
                               
from aula157_package.aula157_m2 import fala_oi #passando o caminho inteiro do package e módulo
                                               #irá funcionar a import do main
                                               #mas para de funciona a execução a partir desse módulo

__all__ = ['variavel', 'soma_do_modulo',] #define o que será importado quando usar *

variavel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y
    
# nova_variavel = 'OK' #não será importada pelo *

#---------------
#aula157_m2.py
#importar para o outro módulo

def fala_oi():
    print('Oi')
#----