print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ") # input = sempre retorna uma string
print("Você digitou: ", chute_str)

# converto para inteiro, para fazer a comparação no if abaixo
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
