#122 Biblioteca copy (cópia rasa e cópia profunda)
# Métodos úteis dos dicionários em Python

# copy - retorna uma cópia rasa (shallow copy)

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

#d2 = d1 #não realiza cópia, apenas apontam para o mesmo local da memória
#d2['c1'] = 1000 #alterando d2 também altera d1

d2 = d1.copy() #cópia rasa

d2['c1'] = 1000 #não irá alterar o outro dicionário, se os itens forem imutáveis
d2['l1'][1] = 999999 #no caso de mutáveis, a cópia rasa apenas aponta para o mesmo local da memória
                     #irá alterar nos dois dicionários

#d2 = copy.deepcopy(d1) #cópia profunda, agora cria uma cópia dos mutáveis também
print(d1)
print(d2)