92 Imprecisão dos números ponto flutuante + round

"""
 Imprecisão de ponto flutuante
 Double-precision floating-point format IEEE 754
 https://en.wikipedia.org/wiki/Double-precision_floating-point_format
 https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2
print(numero_3) #0.79999999
print(f'{numero_3:.2f}')

import decimal #usar apenas em precisão extrema

#aumenta ainda mais casas
 
numero_1 = decimal.Decimal('0.1') #colocar como str para converter exato
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # retorna str
print(round(numero_3, 2)) #arredonda - float