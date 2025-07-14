caminho_arquivo = '187_arquivo.txt' #arquivo txt na pasta raiz

with open(caminho_arquivo, 'w') as arquivo: # quando w é iniciado
                                            # apaga tudo que está no arquivo
    ...

with open(caminho_arquivo, 'a+') as arquivo: # o 'a' não apaga nada
                                             # começa a escrever no final do arquivo
    ...

with open(caminho_arquivo, 'b') as arquivo: # modo binário
    ...

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: #codificar de forma correta o texto
     arquivo.write('Atenção\n') #para caracteres especiais e acentos
                                #aparecerem da forma correta