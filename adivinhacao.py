import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

total_de_tentativas = 3

numero_secreto = 42

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
        print("Você acertou!")
        # total_de_tentativas = 0; #quando usar o while
        break # sai do for

    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


    # total_de_tentativas = total_de_tentativas - 1
    #  QUANDO USAR O WHILE
    # rodada = rodada + 1


print("Fim do jogo")
