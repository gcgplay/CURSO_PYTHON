# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

CAMINHO_ARQUIVO = 'aula207.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

#bd = [p1, p2, p3] #ERRO - A classe não é serializável em json
#jogar em um iterável (lista) para passar para json 
#tem que passar os objetos, convertidos para dict
bd = [vars(p1), p2.__dict__, vars(p3)]

#Envolver o Dump em uma função para que ele não seja importado para B
#Senão ele será executado alterando o arquivo sempre para o modo inicial
#Assim pode se modificar o arquivo json em B, sem que ele volte para o modo inicial
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

#como o dump deve ser executado aqui em A
if __name__ == '__main__':
    fazer_dump()