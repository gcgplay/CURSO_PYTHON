74 Como funciona o for (conhecimento)

"""
Iterável -> str, range, etc método (__iter__) --> te entrega um elemento por vez
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = iter('Luiz') #__iter__() - entregador

print(next(texto)) # => print(texto.__next__()) #L
print(next(texto)) # => print(texto.__next__()) #u
print(next(texto)) # => print(texto.__next__()) #i
print(next(texto)) # => print(texto.__next__()) #z
print(next(texto)) # => print(texto.__next__()) #Erro - StopIteration

texto = 'Luiz' #iterável
iterador = iter(texto)

# while true:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration: #trata o erro
#         break

# é o mesmo que:
for letra in texto:
      print(letra)