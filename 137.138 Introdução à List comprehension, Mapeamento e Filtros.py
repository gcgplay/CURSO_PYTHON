137.138 Introdução à List comprehension, Mapeamento e Filtros

# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#organizar a impressão
import pprint

#função que passa os valores passados para pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero) #gera a mesma lista acima
# print(lista)

#List comprehension
lista = [numero for numero in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = [2 * numero for numero in range(10)] #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(lista)

# Mapeamento de dados em list comprehension
# Tenho uma lista e quero gerar uma nova lista, talvez modificando os dados
# Mas mantendo o mesmo tamanho das listas
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

#lista chave valor
# novos_produtos = [
#     produto
#     for produto in produtos
# ]
# print(*novos_produtos, sep='\n') #{'nome': 'p1', 'preco': 20}
#                                  #{'nome': 'p2', 'preco': 10}
#                                  #{'nome': 'p3', 'preco': 30}

#pode-se realizar comandos e operações dentro da list                                 
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #desempacota o dicionário e aumenta 5% no preço
    if produto['preco'] > 20 else {**produto} #coloca o aumento apenas em preços > 20
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')
#pprint.pprint(novos_produtos, sort_dicts=False, width=40) #ordenamento de chaves, largura em caracteres
p(novos_produtos) #chama a função com o comando acima, que coloca o valor passado em pprint

#FILTRO - restringir determinados valores na lista - retirar o que não quero

lista = [n for n in range(10) if n < 5] #lista comprehension restrita a valores menores que 5
print(lista) #[0, 1, 2, 3, 4]