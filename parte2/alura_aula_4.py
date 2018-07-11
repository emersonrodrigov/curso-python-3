#  TUPLA

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
dias.append("Sábado2")


dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
# dias.append("Sábado2")
print("Tupla criada {}".format(dias))
print("Tupla apos criado nao e possivel adicionar ou remover elementos")

print()
print("tipo tupla {} ".format(type(dias)))



# Lista e Tupla

instrutor1 = ("Nico", 39)
instrutor2 = ("Flávio", 37)

instrutores = [instrutor1, instrutor2]

print( "lista com tuple " , instrutores)


nova_tuple = tuple(instrutores)
print("convertento list to tuple ", nova_tuple)


print("Convertento tuple to list ", list(nova_tuple))



#  colecao do tipo SET, não aceita duplicidade
# Um set é uma coleção não ordenada de elementos. Cada elemento é único,
# isso significa que não existem elementos duplicados dentro do set.

print("COLECAO COM SET -> EVITA DUPLICIDADE")
print("Set não possui indice")
colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677)
colecao.add(11122233344)

print(colecao)

for cpf in colecao:
     print(cpf)

print()
print("Dictionary")
# Para criar um dicionário devemos inicializar os instrutores de um modo um pouco diferente. Veja o código:

instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
print(instrutores)

print("get registro Flávio {}".format(instrutores["Flavio"]))