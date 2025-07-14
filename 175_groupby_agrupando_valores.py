#iterator - agrupar por

from itertools import groupby
 
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

#precisa estar em ordem para funcionar
# alunos = ['a', 'a', 'a', 'a', 'b', 'c']
# grupos = groupby(alunos) 

# for chave, grupo in grupos: #mostra a chave e um grupo com as vezes que essa chave repete
#     print(chave)
#     print(list(grupo))
 
def ordena(aluno):
    return aluno['nota'] #chave de ordenação
 
 
alunos_agrupados = sorted(alunos, key=ordena) #ordenar a lista de dicionario pela nota
grupos = groupby(alunos_agrupados, key=ordena)
 
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)