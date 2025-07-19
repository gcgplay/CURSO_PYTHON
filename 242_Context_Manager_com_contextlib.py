from contextlib import contextmanager

#Criar função decorada - Generator
#Modo tradicional de abrir e fechar um arquivo
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo #pausa no meio do arquivp
                  #executa o with
                  #depois fecha
    except Exception as e:
        print('Ocorreu erro', e)
    #precisa adicionar um tratamento de exceção
    #senão não acessa a exceção e o arquivo não é fechado
    #ou deixar apenas o finally que sempre será executado
    #fechando o arquivo e mostrando o erro
    finally:
        print('Fechando arquivo...')
        arquivo.close()

with MyOpen('aula240.txt', 'w') as arquivo: #cria o arquivo se ele não existir
    # escrever no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

    print('WITH', arquivo)