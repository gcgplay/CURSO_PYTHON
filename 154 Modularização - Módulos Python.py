# 154 Modularização - Módulos Python

# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys
 
import aula154_m #chama e executa o que está no outro módulo (.py)

#-------------
# aula154_m.py
# print('Este módulo se chama', __name__) #main também
# print('Executou aula154_m')
#-------------
 
print('Este módulo se chama', __name__)
 
print(*sys.path, sep='\n') #pastas de instalação do Python

# Este módulo se chama aula154_m
# Executou aula154_m
# Este módulo se chama __main__
# /home/repl/daca4d5f-1d16-4aa7-9dc8-030732f1cfc6
# /usr/lib/python38.zip
# /usr/lib/python3.8
# /usr/lib/python3.8/lib-dynload
# /usr/lib/python3.8/site-packages