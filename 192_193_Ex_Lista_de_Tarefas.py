import os #exceutar comando

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

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer: #se não tiver tarefas para refazer
        print('Nunhuma tarefa para refazer.')
        return #para a execução aqui

    #tira da lista de tarefas a refazer e volta para lista de tarefas
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip() #remove espaços
    if not tarefa: 
        print('Você não digitou uma tarefa')
        return #para a execução aqui

    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear') #limpar o terminal
        continue
    else: #qualquer coisa que não for um dos comandos - adicionar na lista
        adicionar(tarefa, tarefas)
        continue
