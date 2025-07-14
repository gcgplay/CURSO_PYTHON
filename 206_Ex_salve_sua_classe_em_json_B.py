import json

#se fosse necessário fazer o dump, deveria importar a função
from 206_Ex_salve_sua_classe_em_json_A import CAMINHO_ARQUIVO, Pessoa

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2]) #se remover uma pessoa do arquivo json
                              #acontecerá erro caso o index não exista

    print(p1.nome)
    print(p2.nome)
    print(p3.nome)

