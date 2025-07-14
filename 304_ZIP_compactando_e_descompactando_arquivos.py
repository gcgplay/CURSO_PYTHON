import os
import shutil #para apagar pastas
from pathlib import Path #para apagar
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip' #pasta
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip' #zip com os arquivos
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado' #pasta com arquivo desempacotados

# apagar tudo para garantir que está criando do zero
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) 
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) 
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

# criar vários arquivos .txt
def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

#gerar arquivo zip com os arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR): #pasta diretório dos arquivos
        for file in files:
            print(file)
            # zip.write(os.path.join(root, file)) #pega a estrutura completa do diretório
                                                  #User/.../.zip
            zip.write(os.path.join(root, file), file)

#ler o arquivo zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

#extrair os arquivo do zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
            