# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(*args): #recebe uma quantidade ilimitada
                 # de argumentos não nomeados
    print(sum(args))

soma(1, 3, 41, 50)

def soma(a, b, *args): # o args suga tudo que for passado
                       # depois dos parâmentros
    ...

# A / condiciona que os argumentos declarados ANTES dela
# na assinatura da função, não podem ser nomeados
# devem ser apenas valores posicionais

def soma(a, b, /, *, c, **kwargs): #a e b = posicionais
                                   #c deve ser nomeado
                                   #kwargs - tudo nomeado
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')