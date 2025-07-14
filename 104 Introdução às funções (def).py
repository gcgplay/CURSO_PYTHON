104 Introdução às funções (def)

"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do código.
Podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções em Python retornam None (nada).
"""
# Pode usar maiuscula, mas deve se usar letra minúscula no nome da função
# diferencia maisc de minusc
def Print():
    print('1')
    print('2')
    print('3')

Print() 

#parâmetros
def imprimir(a, b, c):
    print("Qualquer coisa")
    print(a, b, c)
    
imprimir(1, 2, 3) #valores = argumentos
imprimir(4, 5, 6) #pode-se alterar os valores

def saudacao(nome='Sem nome'):
    print(f'Olá {nome}!')
    
saudacao('Gabriel') #Olá Gabriel
saudacao() #Olá Sem nome