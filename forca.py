def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavrasecreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")

        for letra in palavrasecreta:
            if (chute == letra):
                print("chute")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
