

#  Manipulando arquivo

print("Criando arquivo com palavras do jogo forca")
arquivo = open("palavras.txt", "w")

arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.write("Morango\n")
arquivo.write("Manga\n")
arquivo.write("Uva\n")
arquivo.write("Abacaxi\n")
arquivo.write("carambola\n")
# Além do r, w e a existe o modificador b que devemos utilizar
# quando queremos trabalhar no modo binário. Para abrir uma imagem devemos usar:

arquivo.close()
print("Arquivo criado com sucesso\n")

print("lendo arquivo com palavras do jogo forca")
arquivo = open("palavras.txt", "r")
print("conteudo completo do arquivo {}".format( arquivo.readlines()))
for linha in arquivo:
    print(linha.strip()) # strip() = remove caracteres especiais / caracteres em branco (direita / esquerda)

#  With fica responsavel por fechar o arquivo, python fica responsavel
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha.strip())