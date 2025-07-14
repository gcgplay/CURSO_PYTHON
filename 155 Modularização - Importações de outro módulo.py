# 155 Modularização - Importações de outro módulo

import aula155_m #chama e executa o que está no outro módulo (.py)
from aula155_m import soma, variavel_modulo

print(aula155_m.variavel_modulo) #5
print(variavel_modulo) #5
print(soma(2, 3)) #5
print(aula155_m.soma(2, 3)) #5

#----------
# aula155_m.py
# variavel_modulo = 'Gabriel'

# def soma (x, y):
#     return x + y