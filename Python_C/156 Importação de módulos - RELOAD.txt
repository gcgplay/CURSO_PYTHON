# 156 Importação de módulos - RELOAD

import importlib
import aula156_m

print(aula156_m.variavel) #Gabriel

for i in range(10):
    #import aula156_m # não imprime nada
                     # singleton - só pode existir uma instância durante toda 
                     # a execução do programa
                     # O Python faz a importação apenas uma vez
                     
    importlib.reload(aula156_m) #para importar várias vezes precisa utilizar 
                                #o RELOAD - recarregar o módulo
                                #ATUALIZA as importações se o módulo for modificado
                        
    
print ('Fim')

#-----
# aula156_m.py
# print(123)

# variavel = 'Gabriel'