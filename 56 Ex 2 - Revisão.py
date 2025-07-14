#56 Ex 2 - Revisão

"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada."""

#Se vai trabalhar com número, você precisa converter para int ou float

# -- Minha resolução --

entrada = input('Digite a hora: ')
hora=int(entrada)

if (hora<=11):
    print('Bom dia')
elif (hora>=12 and hora<18):
    print('Boa tarde')
elif (hora>=18 and hora<24):
    print('Boa noite')
else:
    print('As horas digitadas estão fora do intervalo de 0-24h')

# -- Resolução professor com try/except --

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')


