def soma(x: float, y: float) -> float:
    return x + y

# def main() -> None:
#     print(soma(10, 20))

if __name__ == '__main__': #se o módulo for executado diretamente
                           #será executado como main
                           #os comando abaixo serão executados
    print(soma(10, 20))
    # main()

#se o módulo for importado por outro módulo
#o outro módulo será o main, e o esse modulo terá seu nome original
#os comandos do if não serão executados no outro módulo