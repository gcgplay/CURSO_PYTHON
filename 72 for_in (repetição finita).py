72 for/in - repetição finita

# while - repetições infinitas
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

-- for - repetições finitas --
texto = 'Python'


novo_texto = ''
for letra in texto: #para cada letra no texto
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')