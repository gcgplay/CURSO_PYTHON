# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'

#lista de dicionários
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys() #escreve as chaves do dicionário no aquivo csv
    # nome_colunas = ['Nome', 'Endereço']
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)

    escritor.writeheader() #cabeçalho

    #escreve os valores do dicionário no arquivo csv
    for cliente in lista_clientes:
        escritor.writerow(cliente)