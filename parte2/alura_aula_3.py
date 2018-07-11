# coding: utf-8

# Estrutura de dados: List


valores = []

print("Tipo da variavel valor {}".format(type(valores)))


valores = [0,1,2,3,4]
print("*******************************")
print("**LISTA = > ", valores, "**");
print("*******************************")
print("Tamanho da Lista {}" .format(len(valores)))

print("Menor {}" .format(min(valores)))
print("Maior {}" .format(max(valores)))

print("Pegar valor da posicao 3 da list valores => {}".format(valores[2]) )

print("Verifica se existe valor 0",(0 in valores))
print("Verifica se existe valor 8",(8 in valores))

print("adicionar o elemento 8 na lista")
valores.append(8)
print("Verifica se existe valor 8",(8 in valores))

print("remover o elemento 0 na lista")
valores.pop(0)
print("Verifica se existe valor 0",(0 in valores))
print("*******************************")
print("*******************************")


print()
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores)
print("count {} do valor 0".format(valores.count(0)))

print()
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print("Frutas {}".format(frutas))
print("index da palavra uva", frutas.index('Uva'))
print()

# Exercicio

frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

frutaPedida = input('Qual é a fruta deseja consultar ?')

if(frutaPedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')