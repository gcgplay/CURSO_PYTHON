#Variável livre não está definida dentro do escopo da função

# def fora(x):
#     a = x

#     def dentro():
#         print(locals()) #mostra as variáveis locais que se tem acesso
#         return a # variável livre, pois não está definido no escopo da função dentro
#     return dentro #essa variável dentro também é livre, pois não está definido no escopo da função dentro

# dentro1 = fora(10) # dentro chama a função fora que retorna 
#                   # a função dentro sem executar
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        #valor_final += valor_a_concatenar #tentar passar isso direto gera erro, pois valor_final é uma variável livre
                                           #não está definida dentro do escopo da função interna
                                           #logo não pode ser alterada
        #para que seja possível acessar e alterar o valor da variável declarada no escopo externo
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a') #fixa o valor de valor_final como 'a'
print(c('b')) #'a' se não fizesse a declaração da nonlocal + | como foi feito a nonlocal = ab
print(c('c')) #'a' se não fizesse a declaração da nonlocal + | como foi feito a nonlocal = abc
print(c('d')) #'a' se não fizesse a declaração da nonlocal + | como foi feito a nonlocal = abcd

#------------------