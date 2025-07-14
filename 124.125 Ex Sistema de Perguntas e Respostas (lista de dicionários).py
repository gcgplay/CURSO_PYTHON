#124.125 Ex Sistema de Perguntas e Respostas

#lista de dicionários
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta']) #imprime cada Pergunta
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes): #imprime os índices e as opções
        print(f'{i})', opcao)
    print()
        
    escolha = input('Escolha uma opção: ')
    
    escolha_int = None
    qtd_opcoes = len(opcoes)
    acertou = False
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()
    
    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')
    print()
    
print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')