import random


def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip() # remove espaços direita e esquerda

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


# quando roda o programa via linha de commando , internamente o python preenche uma variavel (__name__),
# desta forma conseguimos separar quando é chamado por linha de comando e quando é chamado
# por outro programa python
if(__name__ == "__main__"):
    jogar()
