"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#### -- CÁLCULO DO PRIMEIRO DIGITO DO CPF -- ####

cpf = '74682489070'

nove_primeiros_digitos = cpf[:9]

contador_regressivo_1 = 10
resultado_digito_1 = 0

# faz todo o cálculo de multiplicação e soma
for digito in nove_primeiros_digitos: #pega cada um dos dígitos
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)

""" ------------------------------------------------
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

#### -- CÁLCULO DO SEGUNDO DÍGITO DO CPF -- ####

dez_primeiros_digitos = nove_primeiros_digitos + str(primeiro_digito)

contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_primeiros_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(segundo_digito)

cpf_gerado_pelo_calculo = f'{nove_primeiros_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido.')
else:
    print('CPF INVÁLIDO.')