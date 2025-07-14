102 Problemas e soluções Validador CPF

#### -- CÁLCULO DO PRIMEIRO DIGITO DO CPF -- ####

#caso o CPF venha com . (pontos)
#cpf = '746.824.890-70'.replace('.', '').replace('-', '') #substitui o . e - por nada

#expressão regular
import re

entrada = input('CPF [746.824.890-70]: ')
cpf = re.sub(
    r'[^0-9]', #tudo que não for um número
    '', #substitui por nada
    entrada
    #'746.pode escrever qualquer coisa, pega somente os números 824.890-70'
)

# VERIFICAR SE TODOS OS DIGITOS SÃO IGUAIS -------------

#primeiro_caractere = entrada[0]
#entrada_sequecial = primeiro_caractere * len(entrada)

#if entrada == entrada_sequencial:
#    print('Entrada INVÁLIDA.')

# -- ou --
import sys

entrada_e_sequecial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

#-----------------------------------------

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