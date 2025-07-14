# Usamos a pathlib para trabalhar com caminhos,
# pastas e arquivos de forma que um código
# funcione em Windows, Linux e Mac.

# Detecta o sistema e converte o caminho de acordo

# Evitar Hard Coding - não utilizar valores fixo no código
# Evitar de escrever todo o caminho manualmente

# ~/Desktop/todo_app/

from pathlib import Path
from shutil import rmtree


caminho_projeto = Path()
# print(caminho_projeto) #imprime caminho relativo - '.'
# print(caminho_projeto.absolute()) #/Users/luizotavio/Desktop/todo_app

caminho_arquivo = Path(__file__) #file - caminho do arquivo
# print(caminho_arquivo) #/Users/luizotavio/Desktop/todo_app/src/pathlib_youtube.py

caminho_pasta = caminho_arquivo.parent #pasta acima de onde estou
# caminho_pasta = caminho_arquivo.parent.parent # pasta anterior - todo_app
# print(caminho_pasta) #/Users/luizotavio/Desktop/todo_app/src


#criar uma nova pasta dentro de uma pasta de determinado caminho
#APENAS GERA um novo caminho - NÃO SALVA NADA
ideias = caminho_arquivo.parent / 'ideias'
print(ideias) #/Users/luizotavio/Desktop/todo_app/src/ideias
print(ideias / 'arquivo.txt') #/Users/luizotavio/Desktop/todo_app/src/ideias/arquivo.txt
print(Path.home()) #/Users/luizotavio
print(Path.home() / 'Desktop')

#CRIAR UM ARQUIVO - APAGAR/ESCREVER/LER
#caminho até o arquivo
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch() #cria o arquivo no caminho especificado
arquivo.unlink() #apaga o arquivo
arquivo.write_text('Olá Mundo') #escrever no arquivo
print(arquivo.read_text()) #ler o arquivo

#Outra maneira
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
#escrever no arquivo
with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')
#ler o arquivo
print(caminho_arquivo.read_text())

#CRIAR UMA PASTA
caminho_pasta = Path.home() / 'Desktop' / 'Nova Pasta'
caminho_pasta.mkdir(exist_ok=True) #se a pasta já existir não faz nada

#cria uma subpasta
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

#criar um novo arquivo dentro da subpasta
outro_arquivo = subpasta / 'outro_arquivo.txt'
outro_arquivo.touch() #cria
outro_arquivo.write_text('Hey') #escreve no outro_arquivo

#se tiver algum arquivo dentro de uma pasta ela não pode ser apagada diretamente
# caminho_pasta.rmdir() #ERRO

#tem que apagar os arquivo mais interno até chegar na pasta raíz

#criar nova pasta
files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

#cria uma pasta com 10 arquivos
for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.exists(): # se o arquivo existir
        file.unlink() # apaga o arquivo

    else:
        file.touch() #cria o arquivo

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt') #escreve o nome do arquivo nele

#função recursiva para entrar na pasta e apagar os arquivos
#pode-se usar o módulo importado rmtree(caminho_pasta) - APAGA TUDO

def rmtree(root, remove_root=True): #root - pasta raíz
                                    #terá o conteúdo da pasta - arquivos e subpastas
    for file in root.glob('*'):
        if file.is_dir(): #entra nos dirétorios (subpastas)
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()
    
    if remove_root:
        root.rmdir()