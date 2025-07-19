# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil

# $HOME
HOME = os.path.expanduser('~') #caminho da pasta do Usuário
# ls \Users\GabrielCG\Desktop
DESKTOP = os.path.join(HOME, 'Desktop') #unir caminho
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs('NOVA_PASTA', exist_ok=True) #cria a pasta se ela não existir
                                         #se já existir ok, não gera erro

#MOSTRANDO COMO FUNCIONA - TEM UMA MANEIRA MAIS SIMPLES
#VER PRÓXIMO ARQUIVO
for root, dirs, files in os.walk(PASTA_ORIGINAL):

    #criar as duas subpastas
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    #copia os arquivos para a nova pasta    
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file) #troca um caminho pelo outro
        
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
        
        # print(caminho_novo_arquivo)
        # print(caminho_arquivo)
        # print(file)
# print(DESKTOP)
# print(PASTA_ORIGINAL)