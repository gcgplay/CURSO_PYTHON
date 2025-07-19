# Abstração
# para logar algo no programa
# Herança = é um

from pathlib import Path

Caminho_arquivo = Path(__file__).parent / log.txt # caminho arquivo .txt

class Log: #super classe
           #contrato que garante que log_error e log_success
           #estarão disponíveis nas outras classes
    def _log(self, msg): # padrão de projeto Template Method
                         # _ não use esse método, ele é para uso interno da classe
        raise NotImplementedError('Implemente o método log')

    # Abstração - método que se quer passar para outras classes
    def log_error(self, msg): #classe abstrata
                              #passa log error para as classes abaixo
        return self._log(f'Error: {msg}') #self é a própria instância da classe

    def log_success(self, msg): # esse métodos de Log são passados para as outras classes
        return self._log(f'Success: {msg}')

# As classes abaixo definem o método Log - Polimorfismo
# Se comporta de diferentes maneiras, de acordo com o tipo de log
# class LogFileMixin(Log): # Adicionar funcionalidades na sua Herança Multipla
                         # Adicionar coisas em outras classes
                         # Não fará parte da família do objeto
#     def _log(self, msg): # sobreposição do método
                         # precisa implementar o método log
#         raise NotImplementedError('msg')

class LogFileMixin(Log):
     def _log(self, msg):
         print(msg)
         msg_fomatada = f'{msg} ({self.__class__.__name__})'
         print('Salvando no log:', msg_fomatada)
         with open(LOG_FILE, 'a') as arquivo: # utiliza 'a', 
         #cria um arquivo log.txt
             arquivo.write(msg_fomatada)
             arquivo.write('\n')

class LogPrintMixin(Log): # é um Log
    def _log(self, msg): 
        print(f'{msg} ({self.__class__.__name__})')

# l = Log()
# l.log('qualquer coisa') # ERRO

if __name__ == '__main__': # se o módulo for main
                           # o método será executado diretamente
    # l = Log()
    # l.log('qualquer coisa') # executando pelo main não terá erro

    # l = LogFileMixin()
    # l.log('qualquer coisa')

    # Devido ao _ não pode chamar o método log aqui
    # deve se chamar log_error
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa') #Error: Qualquer coisa (LogPrintMixin)
    lp.log_success('Que legal')  #Success: Que legal (LogPrintMixin)
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa') # Salvando no log: Qualquer coisa (LogFileMixin)
    lp.log_success('Que legal') # Salvando no log: Que legal (LogFileMixin)
    print(Caminho_arquivo)
# Log é uma classe abstrata
# Não quero que a classe seja executada diretamente
# Não é para usar a classe super (Log) diretamente
# Mas a sua subclasse (mixin)

# 1. Abstração
# A abstração é um conceito fundamental em programação orientada a objetos.
# Ela permite que você defina métodos em uma classe base que serão 
# implementados por classes derivadas. No seu código, a classe Log é uma 
# classe abstrata que define métodos para logar mensagens de erro e sucesso.

# 2. Herança
# Herança é um mecanismo que permite que uma classe derive características 
# (atributos e métodos) de outra classe. A classe Log é a superclasse, 
# e LogFileMixin e LogPrintMixin são subclasses que herdam de Log.

# Método _log: Este é um método abstrato que deve ser implementado pelas 
# subclasses. O prefixo _ indica que é um método interno.
# Métodos log_error e log_success: Estes métodos chamam _log com uma 
# mensagem formatada. Eles são métodos de abstração que serão usados pelas 
# subclasses.

# 4. Polimorfismo
# Polimorfismo permite que métodos em diferentes classes se comportem de 
# maneira diferente, mesmo que tenham o mesmo nome. No seu código, as 
# subclasses LogFileMixin e LogPrintMixin implementam _log de maneiras 
# diferentes.

# Classe LogFileMixin
# Método _log: Aqui, _log é sobrescrito, mas ainda não está implementado.
# Você pode adicionar funcionalidade específica para logar em um arquivo.

# Classe LogPrintMixin
# Método _log: Este método imprime a mensagem no console, incluindo o nome 
# da classe que está executando o log.

# Verificação __name__ == '__main__': Este bloco de código é executado 
# apenas se o módulo for executado diretamente, não quando importado.

# Instância LogPrintMixin: Cria uma instância de LogPrintMixin e chama os
# métodos log_error e log_success.