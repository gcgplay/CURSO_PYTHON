# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True) #apagar a pasta
                                              #ignorar se a pasta não existir
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) #tem que excluir a pasta primeiro
                                            #se ela já existir

# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA') #move e renomeia

shutil.rmtree(NOVA_PASTA, ignore_errors=True)