
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    #implementação dunder methods
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2 #soma de dois pontos
    print(p3) #resultado de __add__ - novoPonto (10, 6)
    print('P1 é maior que p2', p1 > p2) # __gt__
    print('P2 é maior que p1', p2 > p1)

# Os métodos __add__ e __gt__ são chamados implicitamente
# pelos operadores + e > no seu código.

# Quando você faz p3 = p1 + p2, o operador + automaticamente 
# chama o método __add__ da classe Ponto, que retorna um novo 
# objeto Ponto com as coordenadas somadas.

# Quando você faz p1 > p2, o operador > chama o método __gt__, 
# que compara a soma das coordenadas de p1 e p2 e retorna True ou False.