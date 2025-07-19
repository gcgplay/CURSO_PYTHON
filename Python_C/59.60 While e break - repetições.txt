59.60 While e break - repetições

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando a execução de um código não tem fim
"""

condicao = True #se a condição for sempre True = loop infinito

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair': #se o usuário digitar sair = break
        break

print('Acabou')"""

#---

while False: # se a condição sempre for False, o restante do bloco será inalcançável
    print('Meta')
print('Acabou')

#---

contador = 0
 
 while contador <= 10:
     contador = contador + 1
     print(contador)
 
 print('Acabou')