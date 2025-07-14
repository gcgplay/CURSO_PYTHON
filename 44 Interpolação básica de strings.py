#44 Interpolação básica de strings

"""
Placeholders

%s - string
%d e %i - int
%f - float
%x e %X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) #converte o número em hexadecimal com 8 casas decimais.

