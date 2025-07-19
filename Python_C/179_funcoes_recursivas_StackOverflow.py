# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - no retorno, retorna a própria função
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursiva(inicio=0, fim=4):
 
    print(inicio, fim)
 
    # Caso base - para a recursão
    if inicio >= fim:
        return fim #retorna o fim
 
    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim) #Se colocar somente essa parte
                                  #Ocorre um stackoverflow
                                  #excede o número de recursões
 
 
print(recursiva()) #4