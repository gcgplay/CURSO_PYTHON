# with open('aula240', 'w') as arquivo:
# CONTEXT MANAGER - Abrir/Fechar, Conectar/Desconectar
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self): #abre o arquivo
        print('ABRINDO ARQUIVO...')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO...')
        self._arquivo.close()

with MyOpen('aula240.txt', 'w') as arquivo: #cria o arquivo se ele não existir
    # escrever no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

    print('WITH', arquivo)