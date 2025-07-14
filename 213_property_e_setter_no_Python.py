# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        # self.cor_tinta = cor não devem utilizar cor_tinta
        # self._cor = self.cor_tinta # convenção - atributo interno da classe
                                   # _ não utilize esse atributo fora da classe
        self._cor = cor # _cor é privado, pertence a clase
                        # use cor do property e não esse da classe
                        # quando quiser que o atributo seja acessado depois
        self.cor = cor # já acessa diretamente o set
                       # faz o set já no init
        self._cor_tampa = None # não incluido no init - tem que fazer get e set

    #get em Python - obter valor
    @property
    def cor(self):
        print('PROPERTY')
        # return self.cor_tinta
        return self._cor

    #set em Python
    @cor.setter #restringir valores
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito cor Rosa')
        print('Estou no setter', valor) #recebe o valor atribuido a caneta.cor
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

# def mostrar(caneta):
#     return caneta.cor 

    # setter - método utilizado para configurar determinado atributo
    # você quer passar por um método para configurar determinado atributo
    # padroniza o tipo do atributo
    # quando você não quer que utilize outro tipo

    caneta = Caneta('Azul')

    caneta.cor = 'Pink' # ERRO - property não salva valor (método)
                        # informará que não tem um setter configurado

    #getter - obter valor
    print(caneta.cor)
#     mostrar(caneta) #PROPERTY