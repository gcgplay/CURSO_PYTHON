#107 Funções - valores padrões para os parâmetros

"""
 Valores padrão para parâmetros
 Ao definir uma função, os parâmetros podem
 ter valores padrão. Caso o valor não seja
 enviado para o parâmetro, o valor padrão será
 usado.
 Refatorar: editar o seu código.
 """
 
 #Quando existir parâmetros que podem ou não ser usados
 #def soma(x, y, z=0):
 def soma(x, y, z=None): #Definir valor padrão para o parâmetro - None = sem valor
     #if z: #0 - False
     if z is not None:
         print(f'{x=} {y=} {z=}', x + y + z)
     else:
         print(f'{x=} {y=}', x + y)
 
 
 soma(1, 2)
 soma(3, 5)
 soma(100, 200)
 soma(7, 9, 0) #Quando passar qualquer valor para z executa o if
 soma(y=9, z=0, x=7)