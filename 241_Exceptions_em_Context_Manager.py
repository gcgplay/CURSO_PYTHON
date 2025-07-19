# O método __exit__ receberá a classe de exceção, a exceção
# e o traceback. Se ele retornar True, exceção no with será
# suprimida.

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

        # TRABALHANDO EXCEÇÕES
        # criar própria exceção
        # raise class_exception('Minha mensagem')
        # raise class_exception(*exception_.args).with_traceback(traceback_) #montar as informações da exceção

        #pegar informações da exceção
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # return True #Tratei a exceção
                      #Está ciente de um erro
                      #Mas faz o erro passar despespercebido

        # exception_.add_note('Minha nota') #adicionar nota
                                            #acontece a exceção e mostra a mensagem

        #criar/lançar exceção
        #raise ConnectionError('Não deu para conectar')

with MyOpen('aula240.txt', 'w') as arquivo: #cria o arquivo se ele não existir
    # escrever no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

    print('WITH', arquivo)