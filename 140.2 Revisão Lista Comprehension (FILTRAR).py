#140.2 Revisão Lista Comprehension (FILTRAR)

#passa apenas os valores desejados para um novo iterável
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros if numero > 5] #filtra numeros > 5
impares = [numero for numero in numeros if numero % 2 != 0] #filtra impares
pares = [numero for numero in numeros if numero % 2 == 0] #filtra pares
outro_if = [
    numero 
    if numero != 6 else 600 #if antes (condição)
    for numero in pares 
    #if numero % 2 == 0 #if FILTRO PARES
] #filtra pares, se 6 muda para 600


print(numeros) 
print(novos_numeros)
print(impares)
print(pares)
print(outro_if)