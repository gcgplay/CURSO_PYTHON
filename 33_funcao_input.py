# Função input()

#Coleta dados digitados pelo usuário

# nome = input('Qual o seu nome? ') - str
# print(f'O seu nome é {nome}')
# print(f'O seu nome é {nome=}') #imprime também o nome da variável

# pode-se atribuir o valor digitado pelo usuário a uma variável e converter para um determinado tipo
# tudo em uma única linha, MAS NÃO É RECOMENDADO

#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite outro número: '))

# pode ser necessário realizar alguma conferência do dado digitado pelo usuário
# então é melhor separar o dado digitado pelo usuário em uma variável
# e o dado convertido em outra variável

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')