#114 Higher Oder Function - Funções de Primeira Classe

"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns 
(strings, inteiros, etc...)
"""
#---------------------------------------------------------
def saudacao(msg):
    return msg

saudacao_2 = saudacao #aponta para o mesmo local da memória
                      #terá o mesmo retorno

v = saudacao_2('Bom dia')
print(v) #Bom dia

#---------------------------------------------------------

def saudacao(msg): #retorna a msg (3)
    return msg

def executa(funcao, msg): #executa saudacao (2)
    return funcao(msg)
    
v = executa(saudacao, 'Bom dia') #executa executa (1)
print(v)

#---------------------------------------------------------

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args): #restante dos argumentos
    return funcao(*args) #desempacota


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)