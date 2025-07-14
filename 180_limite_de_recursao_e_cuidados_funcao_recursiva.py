# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys

# sys.setrecursionlimit(1004) #DEFINE O LIMITE DE RECURSÕES
 
def factorial(n):
    if n <= 1:
        return 1
 
    return n * factorial(n - 1)
 
 
print(factorial(5))
print(factorial(10))
print(factorial(100))
#print(factorial(1000)) #quebra a recursão do programa