
# Find em String
palavra = "banana";

#  Find retorna o primeiro resultado
print("procurar letra A na {}".format(palavra), palavra.find("a"))

# para encontrar todos os resultados de  em uma string podemosfazer da seguinte form
chute = input("Informa a letra: ")
contador = 0;
for letra in palavra:
    if(letra == chute):
        contador = contador + 1
        print(letra)
print("Foram encontrados {} resultados da palavra {}".format(contador,palavra))

#  Funçoes string
palavra = "BANANA"
print(palavra);

print("{} em minusculo".format(palavra.lower()))
print("{} em maiusculo".format(palavra.upper()))
print("{} em capitalize".format(palavra.capitalize()))

palavra = "  banana   "
print(palavra.strip())



