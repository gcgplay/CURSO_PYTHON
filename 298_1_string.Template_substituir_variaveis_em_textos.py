# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import json
import string
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float | int) -> str:
    brl = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='Gabriel',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='C. G.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

texto = '''
Prezado(a) %nome,

Informamos que sua mensalidade será cobrada no valor de %{valor} no dia %data. Caso deseje cancelar o serviço, entre em contato com a %empresa pelo telefone %telefone.

Atenciosamente,

%{empresa},
Abraços
'''

#SUBSTITUIR TODAS AS VARIÁVEIS MARCADAS COM % NO TEXTO
#PELOS VALORES ATRIBUÍDOS NO DICIONÁRIO
template = string.Template(texto) 
print(template.substitute(dados)) #tem que ter todas as variáveis 
                                  #do texto disponíveis no dict
                                  #gera erro

# print(template.safe_substitute(dados)) #se a variável não estiver 
                                       #declarada em dados, deixa ela em aberto no texto
                                       #não gera erro

