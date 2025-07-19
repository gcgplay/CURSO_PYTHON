import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula298.txt' 

locale.setlocale(locale.LC_ALL, '')

#converte para moeda R$
def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

#determina do delimitador
#onde tiver esse delimitador a variável será substituída por valor
class MyTemplate(string.Template):
    delimiter = '%'

#substitui as variáveis no texto por seus valores em dict
with open(CAMINHO_ARQUIVO, 'r') as arquivo: #usa arquivo txt
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))

