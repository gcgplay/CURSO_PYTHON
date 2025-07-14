"""
 Operação ternária (condicional de uma linha)
 if else em uma linha
 <valor> if <condicao> else <outro valor>
 """

 # print('Valor' if True else 'Outro valor')

 # condicao = 10 == 11 #False
 # variavel = 'Valor' if condicao else 'Outro valor'
 # print(variavel) #Outro valor


 # digito = 9  # > 9 = 0
 # novo_digito = digito if digito <= 9 else 0
 # novo_digito = 0 if digito > 9 else digito #mesma coisa de cima
 # print(novo_digito)

 print('Valor' if False else 'Outro valor' if False else 'Fim') # vários if else - NÃO RECOMENDADO
								# O primeiro True será o resultado