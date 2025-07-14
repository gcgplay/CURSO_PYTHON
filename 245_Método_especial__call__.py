# Método especial __call__
# callable é algo que pode ser executado ()
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # O método call faz a instância/objeto da classe ser executável
    # def __call__(self, *args, **kwargs):
    def __call__(self, nome): 
        print(nome, 'está chamando', self.phone) #executa ação
        return 2134 # retorna valor


call1 = CallMe('23945876545')
retorno = call1('Luiz Otávio')
print(retorno) #2134