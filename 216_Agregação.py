# Agregação (Carro e a Roda) é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos. (Carro tem uma ou mais rodas)
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

# AGREGAÇÃO - Carrinho x Produto
# Um Carrinho agrega um ou mais Produtos
class Carrinho:
    def __init__(self):
        self._produtos = [] #protected - usado dentro da classe
                            #o Carrinho precisa de produtos

    def total(self):
        return sum([p.preco for p in self._produtos]) #list comprehension

    def inserir_produtos(self, *produtos): #enpacota produtos
                                           #método que recebe várias coisas (argumentos não nomeados)
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())