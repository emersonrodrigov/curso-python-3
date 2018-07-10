
# Gerando e arredondando um número aleatório

import random

print(random.random())

#  arredondando um número
print(random.random() * 100)

# convertendo apra inteiro
numero_random = random.random() * 100
print(int(numero_random))

# Definindo o range dos numeros randomicos
for i in range (1,101):
    print(random.randrange(1, 101))