import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    pontos = 1000
    total_de_tentativas = 3

    # numero_secreto =round(random.random() * 100)
    numero_secreto = random.randrange(1, 101) # colocando um range no randomico 1 até 100
    # print('numero secreto',numero_secreto)

    # Aula 7
    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # USANDO WHILE
    # rodada = 1
    # while (rodada <= total_de_tentativas ):

    # USANDO FOR
    for rodada in range(1, total_de_tentativas+1):
        # Interpolação de String
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número: ") # input = sempre retorna uma string
        print("Você digitou: ", chute_str)

        # converto para inteiro, para fazer a comparação no if abaixo
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue # vai para proxima iteração

        # Melhorando a legibilidade do código
        acertou = (chute == numero_secreto)
        maior   = (chute > numero_secreto)
        menor   = (chute < numero_secreto)

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            # total_de_tentativas = 0; #quando usar o while
            break # sai do for

        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            # abs =  numero absoluto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


        # total_de_tentativas = total_de_tentativas - 1
        #  QUANDO USAR O WHILE
        # rodada = rodada + 1


    print("Fim do jogo")


# quando roda o programa via linha de commando , internamente o python preenche uma variavel (__name__),
# desta forma conseguimos separar quando é chamado por linha de comando e quando é chamado
# por outro programa python


if(__name__ == "__main__"):
    jogar()