#utiliza o estado para verificar se é possível executar alguma coisa
#ou se já está sendo executado
#sendo possível alterar esse estado conforme a necessidade
class Camera:
    def __init__(self, nome, filmando=False, fotografando=False):
        self.nome = nome
        self.filmando = filmando #estado/atributo
        self.fotografando = fotografando

    def filmar(self):
        if self.filmando: #True
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True #altera o estado

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar, pois está filmando')
            return
        print(f'{self.nome} está fotografando...')
        self.fotografando = True #altera o estado

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        print(f'{self.nome} parou de filmar')
        self.filmando = False
    
    def parar_fotografar(self):
        if not self.fotografando:
            print(f'{self.nome} não está fotografando')
            return
        print(f'{self.nome} parou de fotografar')
        self.fotografando = False

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar() #Canon está filmando...
c1.filmar() #Canon já está filmando...
print(c1.filmando) #True
print(c2.filmando) #False
c1.fotografar() #Canon não pode fotografar, pois está filmando
c2.fotografar() #Sony está fotografando...
c1.parar_filmar() #Canon parou de filmar
c2.parar_filmar() #Sony não está filmando
c1.parar_fotografar() #Canon não está fotografando
c2.parar_fotografar() #Sony parou de fotografar