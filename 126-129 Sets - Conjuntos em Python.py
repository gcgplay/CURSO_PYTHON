# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis (int, bool, float, ...) como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz') #{'z', 'L', 'i', 'u'} #NÃO GARANTE A ORDEM DOS ELEMENTOS
#s1 = set()  # vazio
#s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados de iteráveis.
#lista_1 = [1, 2, 2, 3, 3, 1]
#set_1 = set(lista_1) #converte em set e elimina repetidos
#lista_2 = list(set_1)
#print(lista_2) #[1, 2, 3]

# - Não aceitam valores mutáveis;
#s1 = {1, 2, [3, 4], {1, 3}} #ERRO

# - Seus valores serão sempre únicos;
# s1 = {1, 2, 3, 3, 3, 3, 1} print(s1) => {1, 2, 3}

# - não tem índexes;
#s1 = {1, 2, 3}
#print(s1[1]) #ERRO

# - não garantem ordem;

# - são iteráveis (for, in, not in)
#print (3 in s1) #True
#for numero in s1:
#   print(numero)

# Métodos úteis:
# add, update, clear, discard
#s1 = set()
#s1.add('Luiz')
#s1.add(2)

#s1.update('Olá mundo') #é adicionado de forma iterada, letra por letra
#s1.update(('Olá mundo', 1, 2, 3)) #adiciona a tupla inteira como um elemento

#s1.discard('Olá mundo') #deleta o valor passado

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #união
s3 = s1 & s2 #intersecção
s3 = s1 - s3 #diferença
s3 = s1 ^ s2 #diferença simétrica - itens que não estão em ambos
print(s3)