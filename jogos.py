import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    
    print("(1) Forca (2) Adivinhação")
    
    jogo = int(input("Qual jogo? "))
    
    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

# quando roda o programa via linha de commando , internamente o python preenche uma variavel (__name__),
# desta forma conseguimos separar quando é chamado por linha de comando e quando é chamado
# por outro programa python
if (__name__ == "__main__"):
    escolhe_jogo()