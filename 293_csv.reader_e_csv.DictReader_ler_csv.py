# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

#caminho absoluto do arquivo
CAMINHO_CSV = Path(__file__).parent / 'aula293.csv'
print(CAMINHO_CSV)

#Em formato de lista
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    # next(leitor) #pula uma linha
    # print(next(leitor))

    for linha in leitor:
        print(linha)
        

#Em formato de dict
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha)
        #pode usar as chaves
        print(linha['Nome'])