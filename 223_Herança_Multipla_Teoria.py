# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Recomendado apenas 3 Hierarquias

# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente (terá tudo das classes anteriores)

# Herança múltipla e mixins (classe que não faz parte daquela família)
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente (classe diferente em cliente)
# Cliente(Pessoa, FileLog) - Cliente herda tudo de Log e Firelog também
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Ao chamar um método herdado em D, haverá diferentes caminhos
# O Python precisa decidir como chegar nesse método
# Python 3 usa C3 superclass linearization para gerar o mro (ordem)
# Você não precisa estudar isso (é COMPLEXO)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)