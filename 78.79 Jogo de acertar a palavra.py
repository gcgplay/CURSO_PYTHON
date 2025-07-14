78.79 Ex Jogo de acertar a palavra

import os #importar módulo

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True: #loop para manter todo o jogo dentro, permite usar break, continue...
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1 #toda vez que voltar no inicio para digitar uma letra irá conta uma tentativa

    if len(letra_digitada) > 1: #verifica se o usuário difitou apenas uma letra
        print('Digite apenas uma letra.')
        continue #volta ao início

    if letra_digitada in palavra_secreta: #verifica se a letra digitada está na palavra secreta
        letras_acertadas += letra_digitada #se a letra digitada for correta ela é adicionada em letras_acertadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas: 
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra secreta:', palavra_formada) #colocar o print fora do for para exibir um caractere ao lado do outro
					       #ao invés de imprimir um por vez, um embaixo do outro

    if palavra_formada == palavra_secreta:
        os.system('clear') #passa o comando clear para o sistema = apagar o conteúdo do terminal
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = '' #zerar tudo 
        numero_tentativas = 0