# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# utiliza closure

# se um objeto estiver fazendo mais coisas do que o necessário
# você deve dividir as tarefas desse objeto

# função decoradora
# recebe uma função e cria uma função interna, gerando uma closure
# a função interna não será executada, mas retornada
# aguardando que sejam passados os argumentos para que ela seja executada

# **kwargs - argumentos nomeados
# *args - argumentos não nomeados 
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar') # dentro da função interna podem ser executadas várias operações
        for arg in args:
            e_string(arg) 
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna
 
 
def inverte_string(string):
    return string[::-1]
 
 
def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('parametro deve ser uma string')
 
 
inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)