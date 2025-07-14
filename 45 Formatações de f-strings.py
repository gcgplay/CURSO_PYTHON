"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a #métodos que serão vistos depois
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}') #adiciona 7 espaços a esquerda para completar 10 caracteres = -------ABC
print(f'{variavel:-<10}.') #adiciona 7 espaços a direita para completar 10 caracteres = ABC-------.
print(f'{variavel:$^10}.') #coloca a variável no centro entre 10 caracteres - $$$ABC$$$$.
print(f'{1000.4873648123746:0=+10,.1f}') # +indicar o sinal, = força o número a aparecer antes dos zeros, 10 caracteres
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') #métodos que serão vistos depois