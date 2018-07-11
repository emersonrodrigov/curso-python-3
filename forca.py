import random


def jogar():
    print(" ********************************* ")
    print(" ** Bem vindo ao jogo de Forca! ** ")
    print(" ********************************* ")

    arquivo = open("parte2/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper() # pegando uma palavra do arquivo
    letras_acertadas = ["_" for letra in palavra_secreta] # List Comprehension
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper() # remove espaços direita e esquerda
        if(chute.upper() in palavra_secreta.upper()):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        acertou = "_" not in letras_acertadas

        print("Palavra correta => {}".format(letras_acertadas))

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")


# quando roda o programa via linha de commando , internamente o python preenche uma variavel (__name__),
# desta forma conseguimos separar quando é chamado por linha de comando e quando é chamado
# por outro programa python
if(__name__ == "__main__"):
    jogar()
