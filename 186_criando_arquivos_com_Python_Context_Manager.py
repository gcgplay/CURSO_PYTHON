# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\GabrielCG\\Desktop\\Nova Pasta\\' #adicionar \\
caminho_arquivo += 'aula116.txt' #concatena para adicionar o nome do arquivo

# ABRIR O ARQUIVO PARA LEITURA
# arquivo = open(caminho_arquivo, 'w')

# sempre FECHAR O ARQUIVO
# arquivo.close()

# Context manager - with (abre e fecha)
with open(caminho_arquivo, 'w') as arquivo: #abre e fecha o arquivo
    print('Olá mundo')
    print('Arquivo vai ser fechado')
