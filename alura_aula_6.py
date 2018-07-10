
# Gerando e arredondando um número aleatório

import random

print(random.random())

#  arredondando um número
print(random.random() * 100)

# convertendo apra inteiro
numero_random = random.random() * 100
print(int(numero_random))

# Definindo o range dos numeros randomicos
for i in range (1,2):
    print(random.randrange(1, 101))


# EXERCICIO

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")


# Usando seed
# Essa entrada também é chamada de seed (semente, em português).
# Entre as chamadas da função random, sempre é utilizado um novo seed.
# Por padrão o Python usa a hora (os milissegundos) como semente, mas nada
# nos impede de definir o mesmo seed antecipadamente. Para isso, existe a função seed!
random.seed(1, 101)
print(random.randrange(100))