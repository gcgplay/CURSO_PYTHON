86 Ex Exibir indice dos elementos da lista

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João') #adicionar novo elemento antes de indices, pois verifica o tamanho da lista


indices = range(len(lista)) #gera uma sequencia de 0 ao tamanho da lista

for indice in indices: 
    print(indice, lista[indice], type(lista[indice]))