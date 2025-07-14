def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Gabriel') 
adiciona_clientes('Joana', cliente1) #adiciona um novo cliente na lista que foi criada
print(cliente1) #['Gabriel', 'Joana']

cliente2 = adiciona_clientes('João') 
adiciona_clientes('Luzia', cliente2) #adiciona um novo cliente na lista que foi criada
print(cliente2) #['Gabriel', 'Joana', 'João', 'Luzia']

# O elementos de cliente1 também ficam salvos em cliente2
# se você usar uma lista como valor padrão, 
# essa lista será compartilhada entre todas as chamadas 
# da função que não especificarem um argumento para lista.

# -- Para corrigir esse problema

# definir cliente1 fora da função
lista1 = []

cliente1 = adiciona_clientes('Gabriel', lista1) 
adiciona_clientes('Joana', cliente1) #adiciona um novo cliente na lista que foi criada
print(cliente1) #['Gabriel', 'Joana']

cliente2 = adiciona_clientes('João') 
adiciona_clientes('Luzia', cliente2) #adiciona um novo cliente na lista que foi criada
print(cliente2) #['João', 'Luzia']

# ou pode-se definir lista como NONE
# sempre que for mutável colocar o parâmetro como None
# assim toda vez que não passar o parâmetro função será None
def adiciona_clientes(nome, lista=None):
    #criar uma condição que crie parâmetro mutavel se ele for None
    if lista is None:
        lista = [] #sempre criará uma nova lista
    lista.append(nome)
    return lista

#lista1 = [] não precisa mais

#Com o if acima, serão criadas duas lista independentes
cliente1 = adiciona_clientes('Gabriel') #não precisará passar a lista, cria uma nova
adiciona_clientes('Joana', cliente1) # para adiciona mais na mesma lista
                                     # deve-se passar a lista, senão será criada outra
cliente1.append('Direto da Silva') # pode adicionar direto
print(cliente1) #['Gabriel', 'Joana']

cliente2 = adiciona_clientes('João') 
adiciona_clientes('Luzia', cliente2) #adiciona um novo cliente na lista que foi criada
print(cliente2) #['João', 'Luzia']