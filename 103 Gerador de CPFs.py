103 Gerador de CPFs

"""Gerador de CPFs"""

import random

#print(random.randint(0, 9)) #Gerador de número aleatório de 0 a 9
#Gerar nove primeiros digitos aleatórios
nove_primeiros_digitos = ''
for i in range(9):
    nove_primeiros_digitos += str(random.randint(0, 9))
print(nove_primeiros_digitos)

#### -- CÁLCULO DO PRIMEIRO DÍGITO DO CPF -- ####
contador_regressivo_1 = 10
resultado_digito_1 = 0

# faz todo o cálculo de multiplicação e soma
for digito in nove_primeiros_digitos: #pega cada um dos dígitos
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(f'O primeiro digito é {primeiro_digito}')


#### -- CÁLCULO DO SEGUNDO DÍGITO DO CPF -- ####

dez_primeiros_digitos = nove_primeiros_digitos + str(primeiro_digito)

contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_primeiros_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f'O segundo digito é {segundo_digito}')

cpf_gerado_pelo_calculo = f'{nove_primeiros_digitos}{primeiro_digito}{segundo_digito}'

print(f'O CPF gerado é {cpf_gerado_pelo_calculo}')