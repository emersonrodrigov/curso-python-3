
palavra_secreta = "banana".upper()
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")


# List Comprehension
# Quando inicializamos a lista, queremos inicializá-la com um caractere _
# para cada letra na palavra secreta. Só que com Python, podemos fazer
# isso diretamente, dentro da inicialização da lista:
caracter = "_"
palavra_secreta = "banana".upper()
letras_acertadas = [caracter for letra in palavra_secreta]
print(letras_acertadas)

print()
print("lista de numeros inteiros com  LIST Comprehension");

inteiros = [1,3,4,5,7,8]

quadrados = [n*n for n in inteiros]
print("Inteiros {} ".format(inteiros))
print("ao quadrado {}".format(quadrados))

print()
print("List Comprehension - Descobrir numeros pares")
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
print("Inteiros {}".format(inteiros))
print("Numeros pares".format(pares))

