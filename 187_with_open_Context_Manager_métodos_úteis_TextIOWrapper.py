caminho_arquivo = '187_arquivo.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n') #insere texto
    arquivo.write('Linha 2\n')
    #print(arquivo.read()) #ERRO - o arquivo foi aberto apenas para escrita
                           #não é permitido leitura
    #fecha arquivo

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read()) #mostra o contéudo do arquivo - leitura

with open(caminho_arquivo, 'w+') as arquivo: #w+ permite escrita e leitura
    print(type(arquivo)) #TextIOWrapper
    arquivo.write('Linha 1\n') #insere texto
    arquivo.write('Linha 2\n')
    arquivo.writelines( #escreve várias linhas (iterável)
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) #retorna o cursor para o inicio
    print(arquivo.read())
    print(arquivo.readline(), end='') #ler linha por linha, tirar quebra de linha
    print(arquivo.readline(), strip()) #ler linha por linha, tirar espaços inicio e fim
    
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): #ler linhas (lista de strings)
        print(linha.strip)