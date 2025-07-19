# method vs @classmethod vs @staticmethod
# method - recebe a instância self, método de instância, tem acesso a tudo da instância
# @classmethod - recebe a própria classe cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'): #método de instância (construtor)
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        #setter - método para definir o valor de um atributo específico
        self.user = user

    def set_password(self, password):
        self.password = password

    #método que crie um usuário, com usuário e senha já configurados
    #class method factory
    #cria uma instância (c1) de Connection com os valores de user e password configurados
    @classmethod
    def create_with_auth(cls, user, password): #cria uma nova instância da classe Connection
        connection = cls() #recebe a classe
        connection.user = user
        connection.password = password
        return connection

    @staticmethod #não tem acesso a nada
                  #função da classe que pode ser acessada externamente
    def soma(x, y):
        return x + y


#c1 = Connection()
c1 = Connection.create_with_auth('Gabriel', '123')
print(c1.user) #None
print(c1.password) #None
c1.set_user('Gabriel')
c1.set_password('123')
print(c1.user) #Gabriel
print(c1.password) #123
print(Connection.soma(2, 3))