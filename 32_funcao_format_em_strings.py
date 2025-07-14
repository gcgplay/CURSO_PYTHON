# Format em strings

#tudo em Python é um objeto, pois possuem métodos (ações/funções)

# Parâmetros são as variáveis listadas na definição de uma função. 
# Eles atuam como placeholders que serão substituídos pelos valores reais quando a função for chamada.

# Argumentos são os valores reais que você passa para a função quando a chama. 
# Eles substituem os parâmetros definidos na função.


#função/método format()

a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a, b, c) #completa cada {} de acordo com a ordem dos argumentos

# se coloca-se mais um {} na string daria o ERRO out of range, pois estaria buscando uma quantidade de valores {} 
# maior do que a quantidade de argumentos passados

string = 'a={0} a={0} b={1} c={2:.2f}' #não daria erro, pois o número indica a posição do elemento desejadom independente da ordem
formato = string.format(a, b, c)

string = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
	nome1=a, nome2=b, nome3=c #nome3 = parâmetro nomeado
)

print(formato)
