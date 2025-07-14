106 Funções - argumentos posicionais e nomeados
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado (posicional) recebe apenas o argumento (valor)
"""
#def soma(x, y):
#    print(x + y)
    
#print(soma) #mostra o local da memória
#print(soma(1, 2)) # mostra 3 e None - já tem print dentro da função
#soma(1, 2) # argumento posicional

def soma(x, y, z): #parâmetros
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3) #argumentos posicionais - dependem da ordem dos parâmetros
soma(1, y=2, z=5) #argumentos nomeados
#soma(1, y=2, 3) #ERRO - se um for nomeado, todos depois dele devem ser nomeados

print(1, 2, 3, sep='-')