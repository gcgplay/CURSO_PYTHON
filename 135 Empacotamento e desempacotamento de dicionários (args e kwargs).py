135 Empacotamento e desempacotamento de dicionários (*args e **kwargs)
a, b = 1, 2
a, b = b, a
# print(a, b) #2 1


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa
# print(a, b) #nome sobrenome - imprime as chaves

# a, b = pessoa.values()
# print(a, b) # Aline Souza - imprime os valores

# a, b = pessoa.items()
# print(a, b) #('nome', 'Aline') ('sobrenome', 'Souza') - imprime um tupla chave/valor

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a1) #nome Aline
# print(b1, b2) #sobrenome Souza

# for chave, valor in pessoa.items():
#     print(chave, valor) #nome Aline
#                         #sobrenome Souza
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#juntar dois dicionários 
# desempacotamento = **extrai os valores de um dicionário
pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args (não nomeados) e kwargs (nomeados)
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados) - empacotar


def mostro_argumentos_nomeados(*args, **kwargs): #empacotando os argumentos
    print('NÃO NOMEADOS:', args) #se passar argumentos não nomeados 1 e 2 por exemplo, eles aparecerão separados (1, 2)
    # print(kwargs) #{'nome': 'Joana', 'qlq': 123}

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa) #desempacota o dicionário

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)