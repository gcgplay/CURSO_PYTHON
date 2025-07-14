108.109 Escopo de funções, variáveis locais e globais
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
O que for definido dentro da função fica protegido dentro do escopo da função
Não irá afetar o que está fora da função
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""
#def escopo():
#    x = 1 #definido dentro da função
#    print(x)
    
#print(x) #ERRO - x não pode ser acessado fora da função
#--------------------------------------------------------------
# o x pode ser definido fora, mas antes da chamada da função
#def escopo():
#    print(x)

#x = 1 #definido fora da função
#escopo()
#--------------------------------------------------------------
#x = 1

#def escopo(): #essa função tem acesso a x, mas não tem acesso à variável y
#    def outra_funcao(): #tem aceso a x e a y
#        y = 2 #definido dentro de outra_funcao
#        print(x, y)
        
#    outra_funcao() #executada dentro do escopo da função escopo    
#    print(x)

#escopo() #chama a função escopo no escopo global
#--------------------------------------------------------------
#x = 1

#def escopo(): 
    #x = 10 #diferente do x externo, passa a ser o x definido dentro da função
            #não altera o x externo
#    def outra_funcao(): 
#        y = 2 
#        print(x, y) #irá puxar do x definido na função escopo
        
#    outra_funcao() #executada dentro do escopo da função escopo    
#    print(x)

#print(x) #1 (externo)
#escopo() #10 2 (outra_funcao)
          #10 (escopo)
#print(x) #1 (externo)
#--------------------------------------------------------------
x = 1

def escopo():
    global x #para tornar a variável global, será a mesma definida fora do escopo da função
    x = 10 #altera a variável x externa

    def outra_funcao():
        global x 
        x = 11 #altera o x externo
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x) #antes de chamar a função escopo - 1
escopo() # altera x -> 10 -> 11
print(x) #11
#---------------------------------------------------------------
#Durante a execução o interpretador para a execução do escopo principal
#para executar o escopo da função quando ela é chamada
#é criado um lugar na memória para executar a função
#quando executa a outra função também pausa a execução dos escopos externos
#CALL STACK - mostra escopo e módulo
#Assim, as variáveis definidas no escopo da função são definidas em outro local da mémoria
#Por isso não interferem no valor das variáveis externas