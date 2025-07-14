#dicionário
#o modulo json já faz a conversão dos dados entre as linguagens
import json

### --- O CÓDIGO ABAIXO SALVA OS DADOS NO ARQUIVO JSON --- ###
# pessoa = {
#     'nome': 'Gabriel Carmo',
#     'sobrenome': 'Guimarães',
#     'enderecos': [
#         {'rua': R1, 'numero': 32},
#         {'rua': R2, 'numero': 25},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': {2, 4, 6, 8, 10},
#     'dev': True,
#     'nada': None,
#     #'set': {1, 2, 3} ERRO, formato set não é serializavel para json
# }

# NÃO ESQUECER O ENCODING, para não ocorrer problemas com caracteres
# with open('aula190.json', 'w', encoding='utf8') as arquivo:
#     #json.dump(pessoa, arquivo) # joga os dados do objeto pessoa
#                                # no arquivo json, no formato de caracteres
#                                # da tabela ascii
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) # para salvar os dados
#                                                              # sem a formatação ascii
#                                                              # com organização dos dados
#     #json.dumps() #para string

# Não suporta funções, métodos - somente coisas simples

### A SEÇÃO ACIMA FOI COMENTADA, POIS OS DADOS JÁ FORAM PASSADOS PARA O ARQUIVO JSON
### --- O CÓDIGO ABAIXO LÊ OS DADOS NO ARQUIVO JSON --- ###

with open('aula190.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa) # dicionário em Python
    print(pessoa['nome']) #acessar os dados do arquivo json

