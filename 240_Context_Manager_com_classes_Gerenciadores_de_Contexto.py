# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

# Classe utilizada com with
# Duck Typing - tipagem dinâmica - não olhar o tipo
# Se o objeto possui os métodos necessários de determinado tipo
# O Python irá considerar esse objeto como esse sendo desse tipo

# Ex de Context Manager:
# with open('aula240.txt', 'w') as arquivo:
#   ...

# COMO IMPLEMENTAR A ABERTURA DE ARQUIVO ACIMA - arquivo 2

class MyContextManager:
    def __init__(self):
        print('INIT')

    def __enter__(self):
        print('ENTER')
        return 1234 # vai para alguma_coisa

    def __exit__(self, class_exception, exception_, traceback_): # _ apenas para diferencia da linguagem
        print('EXIT')

instancia = MyContextManager()

#with MyContextManager() as alguma_coisa:
with instancia as alguma_coisa:
    print(alguma_coisa) # recebe o retorno no enter
    print('WITH')

# ENTER -> WITH -> None -> EXIT