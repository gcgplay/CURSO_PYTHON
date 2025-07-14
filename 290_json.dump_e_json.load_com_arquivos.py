#dump - jogar pra fora - arquivo
#load - carregar pra dentro - arquivo

import json
import os

NOME_ARQUIVO = 'aula177.json'
# abspath - caminho lá da raiz (C:) até o local do arquivo
# cria o caminho completo dir + arquivo
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), #nome do diretório do arquivo
        NOME_ARQUIVO 
    )
)

# string_json = '''
# {
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": true,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": [
#     "Frodo",
#     "Sam",
#     "Gandalf",
#     "Legolas",
#     "Boromir"
#   ],
#   "budget": null
# }
# '''
# print(json.loads(string_json))

#pega o resultado do print json --> dict
#dict
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

#criar um arquivo e salvar esse dicionário - w - escrever
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)


#ler arquivo json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)

print(filme)

