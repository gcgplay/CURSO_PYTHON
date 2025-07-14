# 144 dir, hasattr e getattr em Python

#Na aba DEBUG CONSOLE, modo interativo, comando dir(string) -> mostra todos os atributos definidos para str

string = 'Luiz'
metodo = 'strip' #nome do método

#hasattr - verifica se determinado objeto tem determinado atributo (nome, por exemplo)
if hasattr(string, metodo): #verifica se a str possui determinado método
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)


class Pessoa:
    nome = "João"

p = Pessoa()
print(hasattr(p, 'nome')) # True
print(hasattr(p, 'idade')) # False