# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)
 
        def sua_nova_funcao(*args, **kwargs):
             res = func(*args, **kwargs)
             final = f'{res} {nome}'
             return final
        return sua_nova_funcao
    return decorador
 
 
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1') #serão aplicados de baixo para cima
def soma(x, y):
     return x + y
 
 
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

#Decorador: 1
#Decorador: 2
#Decorador: 3
#Decorador: 4
#Decorador: 5
#15 1 2 3 4 5
