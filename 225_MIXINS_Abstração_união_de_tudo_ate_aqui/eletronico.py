from log import LogPrintMixin #pode apenas alterar para LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome # _ uso interno
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin): #Herança Multipla
    def ligar(self):
        super().ligar() # passa a chamada para para a classe pai
                        # não perde a funcionalidade do método
                        #recebe novos métodos por herança
        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

# PREFIRA COMPOSIÇÃO AO ÍNVES DE HERANÇA
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)