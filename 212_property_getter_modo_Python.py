# getter - método utilizado para obter um valor de 
# determinado atributo
# NO PYTHON - se comporta como atributo
# property - é uma propriedade do objeto, método (def) que
# se comportada como atributo
# Geralmente a property é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        # Em outras linguagens teria os modulos de proteção
        # private, protected, public - encapsulamento
        # self.cor = cor
        self.cor_tinta = cor #precisou alterar o nome do atributo

    # para conceder acesso a um atributo protegido
    # cria-se um get concedendo acesso
    # def get_cor(self):
    #     # pode ser usado também para executar uma ação
    #     # quando for chamado
    #     print('Chamei o get')
    #     return self.cor

    # NO PYTHON É UTILIZADO O PROPERTY
    # Método que se comporta como atributo - NÃO PODE SER CHAMADO COM ()
    @property
    def cor(self):
        print('Executa uma ação')
        return self.cor_tinta # ao alterar o nome do atributo
                              # irá alterar o nome apenas nesse método

# imagine que esse comando para acessar a cor da caneta
# esteja sendo utilizado em vários locais do programa
# código cliente - código que usa seu código em outros locais
caneta = Caneta('Azul')
print(caneta.cor) # quando chamar .cor = .cor_tinta do @property
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

# Com o get, caso fosse alterado o nome da variavel
# não seria necessário alterar o nome da variável
# em todo o código, pois ela estaria sendo acessada
# por get_cor

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

