# Conta será uma classe abstrata
# Terá o método abstrato sacar
# Agência, Nº, Saldo como atributos
# E método deposito
# subclasses deve implementar o método sacar
# COM TIPAGEM
import abc

class Conta(abc.ABC):

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #método abstrato
    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

    
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.sacar - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite): #mesmo init da super classe
                                                       #limite é um atributo adicional de CC
        super().__init__(agencia, conta, saldo) #vai para a super classe
        self.limite = limite #da conta corrente

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.sacar - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0) #saldo 0
    cp1.sacar(1) # Não foi possível sacar o valor desejado
    cp1.depositar(1) #Saldo 1
    cp1.sacar(1) #Saldo 0
    print('----')
    cc1 = ContaCorrente(111, 222, 0, 100) #saldo 0
    cc1.sacar(1) #Saldo -1
    cc1.depositar(1) #Saldo 0
    cc1.sacar(1) #Saldo -1
    cc1.sacar(1) #Saldo -2
    cc1.sacar(98) #Saldo -100
    cc1.sacar(1) #Não foi possível sacar o valor desejado
