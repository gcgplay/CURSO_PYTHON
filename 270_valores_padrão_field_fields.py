from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
    # nome: str = 'Missing'
    nome: str = field(
        default='MISSING'
    )
    sobrenome: str = 'Not sent'
    idade: int = 0 #atribui um valor padrão
                   #somente valores IMUTÁVEIS
    
    #todos declarados após declarado valor padrão
    #devem também possuir valor padrão

    # enderecos: list[str] = [] #ERRO - Lista é Mutável - usar field
    enderecos: list[str] = field(default_factory=list) #argumento nomeado
                                                       #fabrica mutável
                                                       #chama a função list e list cria uma nova lista
if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1)) #mostra os metadados da classe - configurações dos campos
    print(p1)