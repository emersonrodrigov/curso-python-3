import random


def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")



    print("Fim do jogo")

# quando roda o programa via linha de commando , internamente o python preenche uma variavel (__name__),
# desta forma conseguimos separar quando é chamado por linha de comando e quando é chamado
# por outro programa python
if(__name__ == "__main__"):
    jogar()
