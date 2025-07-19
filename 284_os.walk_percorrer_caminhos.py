# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

#entra em cada uma das pastas, até a última subpasta, até o último arquivo

import os
from itertools import count

caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
counter = count() #criar um contador

#mostra o caminho de cada pasta
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root) #numerar o loop atual

    #mostra os diretórios/subpastas dentro das pastas
    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    #mostra os arquivos dentro das subpastas
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_) #completo
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)

#     0 Pasta atual CAMINHO...
#         Dir: SUBPASTA1
#         Dir: SUBPASTA2
#         FILE: Nome do arquivo
#     1 Pasta atual CAMINHO...
#         Dir: SUBPASTA1
#         Dir: SUBPASTA2
#         FILE: Nome do arquivo