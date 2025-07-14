70 while - qual letra aparece mais vezes

#frase = 'O Python é uma linguagem de programação multiparadigma. '\
#	'Python foi criado por Guido van Rossum.' #caso necessário, usar .upper() ou .lower()

#print(frase.count('Python')) #2 #diferencia maiusc de minusc
#print(frase.count('o') #9

#----
frase = 'aaaooo'

i = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Iteração letra por letra
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': # não contar espaço
        i += 1 #precisa atualizar o valor de i, para pular para a próxima letra
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual) #salva a letra que apareceu mais vezes até o momento

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual: #compara a quantidade da letra anterior com a atual
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

