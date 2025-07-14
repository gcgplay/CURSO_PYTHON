# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception): #padrão usar Error no nome da classe
                          #criar uma classe que herda de Exception
    ...

class OutroError(Exception): #padrão usar Error no nome da classe
                          #criar uma classe que herda de Exception
    ...

def levantar():
    # raise MyError('Mensagem de erro') #nunca retorna
    
    #jogando a excessão em uma variável
    exception_ = MyError('a', 'b', 'c') # mais de uma excessão - args
    exception_.add_note('Faça tal coisa')
    raise exception_

# levantar()

#tratar a excessão
try:
    levantar()
except MyError as error:
    print(error.__class__.__name__)
    print(error) # imprime somente a mensagem
    exception_ = OutroError('Vou relançar a excessão')
    exception_.add_note('Outra nota')
    #relançar excessão
    raise exception_ from error