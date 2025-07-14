63 while + while (laços internos)

qtd_linhas = 5
qtd_colunas = 5
 
linha = 1
while linha <= qtd_linhas: # para cada linha haverá 5 colunas
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}') #linha=1 coluna=1
        coluna += 1
    linha += 1
 
print('Acabou')