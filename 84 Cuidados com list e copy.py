84 Cuidados com list e copy

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#---
lista_a = ['Luiz', 'Maria']
lista_b = lista_a # não faz uma cópia da lista_a, mas faz lista_b apontar para o mesmo endereço na memória

# se for feita uma alteração em lista_a também será alterada a lista_b
lista_a[0] = 'Alteração'
print(lista_b) #['Alteração', 'Maria']

#--
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #faz uma cópia da lista_a

#dessa forma se alterar a lista_a não altera a lista_b
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)