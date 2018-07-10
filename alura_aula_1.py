

print("ola mundo")


# -- entendendo como funciona a função help
# help()

# Help comando print



help(print) # ajuda interativa
# value é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.
# sep é o separador entre os valores, por padrão o separador é um espaço em branco.
# end é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n)

print("Brasil", "ganhou", 5, "titulos mundiais", 'USANDO SEP',sep="-" )
print("Brasil", "ganhou", 5, "titulos mundiais", end="\n")


# DECLARANDO VARIAVEIS
pais = "Italia"
quantidade = 4

print(pais, "ganhou", quantidade, "titulos mundiais ")

print( 'Tipo da variavel pais' , type(pais) , 'str = string' )
print( 'Tipo da variavel quantidade' , type(quantidade), 'int = inteiro' )

print()
pais = "Brasil"
print('Python é uma linguagem dinamica')
print( 'o valor da variavel pais é:',  pais , 'e o tipo é: ', type(pais) )

pais = 644
print( 'o valor da variavel pais é:',  pais , 'e o tipo é: ', type(pais) )

print('o tipo da variável é definido de acordo com o valor que ela guarda, isso faz parte da tipagem dinâmica do Python.')
print()
print('Exemplo de syntax_sugar => Um syntax sugar, docinho de sintaxe da linguagem, apenas simplifica algo que seria '
      'trabalhoso, mas não muda a característica da linguagem')
numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
