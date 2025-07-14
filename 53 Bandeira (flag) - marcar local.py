"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = mostra a identidade do elemento na memória
"""

#v1 = 'a'
#v2 = 'a'
#print(id(v1))
#print(id(v2))
#O Python percebe que o valor das variáveis é igual e faz ela apontarem para o mesmo endereço da memória

#Verificar se o interpretador já leu/passou em determinado trecho do código

condicao = False #pula o if
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')