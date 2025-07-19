62 while + CONTINUE - pulando uma repetição

contador = 0
 
 while contador <= 100:
     contador += 1
 
     if contador == 6: #pula o contador 6
         print('Não vou mostrar o 6.')
         continue
 
     if contador >= 10 and contador <= 27: #pula o contador de 10 a 27.
         print('Não vou mostrar o', contador)
         continue
 
     print(contador)
 
     if contador == 40:
         break
 
 
 print('Acabou')