# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais

# SO"L"ID
# S - Single Responsibility Principle (Princípio da Responsabilidade Única):
# Cada classe deve ter uma única responsabilidade ou motivo para mudar. Isso 
# significa que uma classe deve fazer apenas uma coisa e fazer bem.

# O - Open/Closed Principle (Princípio Aberto/Fechado):
# As classes devem estar abertas para extensão, mas fechadas para modificação. 
# Ou seja, você deve poder adicionar novas funcionalidades sem alterar o código existente.

# L - Liskov Substitution Principle (Princípio da Substituição de Liskov):
# Objetos de uma classe derivada devem poder substituir objetos da classe base 
# sem alterar o comportamento do programa. Isso garante que a herança seja usada corretamente.

# I - Interface Segregation Principle (Princípio da Segregação de Interfaces):
# Muitas interfaces específicas são melhores do que uma única interface geral. 
# Isso significa que os clientes não devem ser forçados a depender de interfaces que não utilizam.

# D - Dependency Inversion Principle (Princípio da Inversão de Dependência):
# Módulos de alto nível não devem depender de módulos de baixo nível. 
# Ambos devem depender de abstrações. Além disso, abstrações não devem depender de detalhes; 
# detalhes devem depender de abstrações.

# POLIMORFISMO -------------------------------------------

# Classe Log (superclasse)

# classes derivadas de uma mesma superclasse
# class LogFileMixin(Log): 
    # def _log(self, msg): # métodos iguais (com mesma assinatura)
    # ...

# class LogPrintMixin(Log):
    # def _log(self, msg):
    # ... # mas comportamentos diferentes.

# ---------------------------------------------------------

# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

# Onde você usar Log, qualquer subclasse da superclasse deve substituí-la
# sem interferir na funcionalidade da aplicação

# ---------------------------------------------------------
# Sobrecarga de métodos (overload)  🐍 = ❌ (Python não suporta)
# Sobreposição de métodos (override) 🐍 = ✅
# Sobrescrever o método da subclasse na superclasse
from abc import ABC, abstractmethod

class Notificacao:
    def __init__(self, mensagem) -> None: #método retorna None
        self.mensagem = mensagem

    #classes abstratas não podem ser estanciadas até que o método seja concreto
    @abstractmethod 
    def enviar(self) -> bool: ... # informar o tipo de retorno aos outros desenvolvedores

# class NotificacaoEmail(Notificacao):
    # def enviar(self): #como foi determinado que enviar retorna bool
                        #como não houve esse retorno então ficou None
        # print('Enviando e-mail: ', self.mensagem)

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: 
        print('Enviando e-mail: ', self.mensagem)
        return True # Foi enviada

# class NotificacaoSMS(Notificacao):
    # def enviar(self): #None
        # print('Enviando SMS: ', self.mensagem)

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool: #None
        print('Enviando SMS: ', self.mensagem)
        return False # Não foi enviada

# POLIMORFISMO
def notificar(notificacao: Notificacao): #puxa todos os métodos da classe determinada
                                         #o objeto notificacao é polimorfico, muda sem quebrar a app
    notificação_enviada = notificacao.enviar() #verifica se a notificação foi enviada

    if notificação_enviada:
        print('Notificação enviada')

    else:
        print('Notificação NÃO enviada') #sendo None o retorno de enviar
                                         #sempre retorna o else

notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)

n = NotificacaoSMS('Testando notificação')
n. enviar()