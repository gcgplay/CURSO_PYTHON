# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

# Abstração que pode ter um grupo de coisa para escolher
# Simulando a direção de um personagem em um jogo
import enum

#um tipo com membros
#Dessa forma o tipo fica Any
#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
class Direcoes(enu.Enum): #assim será do tipo Direcoes
    ESQUERDA = 1
    DIREITA = 2
    ACIMA = enum.auto()
    ABAIXO = enum.auto()
print(Direcoes(1), Direcoes('ESQUERDA'), Direcoes.ESQUERDA) #por valor ou por chaves
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

#def mover(direcao): #não reconhece o tipo de direcao
def mover(direcao: Direcoes): #especifica o tipo, mesmo assim não reconhece o tipo

    # if direcao not in ['esquerda', 'direita']:
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    #direcao. -> Any
    #declarando a classe será possível acessar direcao.

    # print(f'Movendo para {direcao}')
    print(f'Movendo para {direcao.name} ({direcao.value})') 

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('direita')
# mover('esquerda')
# mover('lado') #Erro - Direção não encontrada