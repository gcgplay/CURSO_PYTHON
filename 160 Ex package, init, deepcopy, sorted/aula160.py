import copy

from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

#list comprehension - mapeamento adicionando 10%
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} #gera um dict e espande os produtos
                                               #criar de novo a chave 'preço' e subir 10%
    for p in copy.deepcopy(produtos) #não tinha nessecidade de fazer deepcopy
                                     #não altera a lista original
]
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

#DEVE-SE REALIZAR PRIMEIRO A CÓPIA ANTES DE FAZER QUALQUER ALTERAÇÃO
#POIS PODE OCORRER DE MODIFICAR OS DADOS ORIGINAIS

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['nome'] #também não alterou nenhum dado da lista original
)
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
 # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
 produtos_ordenados_por_preco = sorted(
     copy.deepcopy(produtos),
     key=lambda p: p['preco']
 )
 
 # FINAL
 
 print(*produtos, sep='\n')
 print()
 print(*novos_produtos, sep='\n')
 print()
 print(*produtos_ordenados_por_nome, sep='\n')
 print()
 print(*produtos_ordenados_por_preco, sep='\n')