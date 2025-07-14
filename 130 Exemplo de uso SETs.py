130 Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ') 
    letras.add(letra.lower()) #adiciona a letra digitada pelo usuário no set
			      #não registra repetidos

    if 'l' in letras: #verifica se a letra desejada foi digitada
        print('PARABÉNS')
        break

    print(letras)