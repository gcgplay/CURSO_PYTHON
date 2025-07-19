# conversão de tipos, coerção, type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print (1 + 1) #realiza a operação de soma
print ('a' + 'b') #faz a concatenação das strings
print ('1' + 1) #ERRO - tenta concatenar string com int, tipagem forte
#se fosse feito o print acima em tipagem fraca (javascript/php)
#seria convertido um tipo em outro
print(int('1'), type(int('1'))) #converte para int e mostra o tipo
print(type(float('1') + 1)) #retorna resultado em float
print(bool(' ')) #considerada True
print(str(11) + 'b') #converte o int em str para não dar ERRO