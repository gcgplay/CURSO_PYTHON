import os #exceutar comando
import json

def listar(tarefas):
    print()
    if not tarefas: #se não tiver tarefas
        print('Nunhuma tarefa para listar.')
        return #para a execução aqui
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}') #tab

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas: #se não tiver tarefas
        print('Nunhuma tarefa para desfazer.')
        return #para a execução aqui
    
    #desfaz a última tarefa da lista e atribuir a uma variável
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    #adiciona a tarefa removida em tarefas_refazer
    tarefas_refazer.append(tarefa)
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer: #se não tiver tarefas para refazer
        print('Nunhuma tarefa para refazer.')
        return #para a execução aqui

    #tira da lista de tarefas a refazer e volta para lista de tarefas
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip() #remove espaços
    if not tarefa: 
        print('Você não digitou uma tarefa')
        return #para a execução aqui

    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada na lista de tarefas.')
    listar(tarefas)

#lê o arquivo json
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas)
        
#salva a lista de tarefas e as modificações no arquivo json
def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula195.json'
tarefas = ler(CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas), #ERRO - else
    }

    # comando = comandos.get(tarefa)() #erro - else
    comando = comandos.get(tarefa) if comandos.get(tarefas) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
