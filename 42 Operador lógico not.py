# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

#if senha == '123456':
	#print('Entrou')
#else:
	#print('Senha incorreta')

#-- OU --

if senha != '123456':
	print('Senha incorreta')

#-- OU --

if not senha:
	print('Você não digitou nada.')

print(not 0) #True
print(not True) # False
print(not False) # True