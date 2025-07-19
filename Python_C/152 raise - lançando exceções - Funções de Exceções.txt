# 152 raise - lançando exceções

# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

#print(123)
#raise ValueError('Erro aqui') #você lança um erro qualquer, onde quiser
#print(456)

#não se deve lançar exceções para erros já lançados pelo próprio Python
# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError: #cria uma exceção caso aconteça esse erro
#         print("Alguma coisa que fosse necessária em caso de erro")
#         return n #retorna o próprio numero
#         raise #relança o próprio erro, mesma coisa que o Python já faz

#Criar seu próprio erro e tratar o erro
#Função que verifica se o número (divisor) é 0
#Lança uma exceção ou retorna True
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

#Verifica se o que foi passado é int ou float
def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

#função que usa as outras funções com execeções
#se tudo ok, retorna o resultado, se não lança execeções
def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))