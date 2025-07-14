#map, filter e reduce

from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n') # * desempacota os itens (dicionarios) do iterador
                                     # convertendo em lista
                                     # e imprime um por um
    print()

#lista de dicionários
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial( #função que vai receber uma função e parte de seus argumento
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} # ** desempacota e cria uma cópia
                                                        # usando a função aumentar_dez_porcento
                                                        # para modificar o preço em cada dicionário da lista
#     for p in produtos # para cada item (dicionário) da lista produtos
#                       # adiciona uma cópia à lista novos_produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto, #cria uma cópia do dicionário
        'preco': aumentar_dez_porcento(
            produto['preco'] #atualiza o valor de preço passando-o como parâmetro de aumentar_dez_porcento
        )
    }


novos_produtos = list(map( #Aplica a função muda_preco_de_produtos a cada item da lista produtos.
                           #Converte o objeto map (que é um iterador) em uma lista.
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)