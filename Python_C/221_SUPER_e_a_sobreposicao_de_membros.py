# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# str = classe
# cria-se uma nova classe para estender alguma funcionalidade
class MinhaString(str): # herda tudo de str
                        # MinhaString é str
    def upper(self): # não usa mais o método upper de str
        # return 'ABC' # ao inves de colocar as letras maiusculas
                       # agora retorna ABC
        # se quiser, pode adicionar algum comando
        print('CHAMOU UPPER')
        # e chamar o método original da classe pai
        return super().upper()

string = MinhaString('Gabriel')
print(string.upper()) #GABRIEL