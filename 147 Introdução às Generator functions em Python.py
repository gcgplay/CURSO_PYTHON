# 147 Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 #Pausar
    print('Continuando...')
    yield 2 #Pausar
    print('Mais uma...')
    yield 3 #pausado
    print('Vou terminar') #não chega aqui
    #else 'Acabou'
    
gen = generator(n=0)
print(next(gen)) #1
print(next(gen)) #Continuando 2
print(next(gen)) #Mais uma 3

for n in gen:
    print(n)

def generator(n=0, maximum=10):
    while True:
        yield n # Em vez de retornar um valor e encerrar, 
                # ela pausa a execução e retorna o valor de n ao chamador
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000)
for n in gen:
    print(n)