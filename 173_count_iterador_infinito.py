# count é um iterador sem fim (itertools)

#contador infinito

from itertools import count
 
# c1 = count() #infinito

# print(next(c1)) #1
# print(next(c1)) #2

c1 = count(step=8, start=8) #(pulo, inicio)
r1 = range(8, 100, 8) #(inicio, fim, pulo)
 
print('c1', hasattr(c1, '__iter__')) #é um iterável
print('c1', hasattr(c1, '__next__')) #é um iterator
print('r1', hasattr(r1, '__iter__')) #é um iterável
print('r1', hasattr(r1, '__next__')) #não é um iterator
 
print('count')
for i in c1:
    if i >= 100:
        break
 
    print(i)
print()
print('range')
for i in r1:
    print(i)