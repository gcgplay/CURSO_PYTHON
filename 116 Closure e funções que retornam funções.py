#116 Closure e funções que retornam outras funções

"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao): #função que cria saudação
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar #registro na memória

#s1 = criar_saudacao('Bom dia', 'Luiz')
#s2 = criar_saudacao('Boa noite', 'Luiz')

#print(s1()) #closure - quando fecha a chamada da função s1, que retorna a função criar_saudacao
#print(s2())

falar_bom_dia = criar_saudacao('Bom dia') #cria a função para falar Bom dia
falar_boa_noite = criar_saudacao('Boa noite') # cria a função para falar Boa noite

for nome in ['Maria', 'Joana', 'Luiz']: 
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))