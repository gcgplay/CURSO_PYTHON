64 Ex Iterando strings com while

#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

#nova_string += '*L*u*i*z* *O*t*á*v*i*o' #adicionar um * entre cada caractere da string

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}' #adiciona letra por letra com * em novo_nome
    indice += 1

novo_nome += '*'
print(novo_nome)