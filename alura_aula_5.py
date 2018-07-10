

# Para saber mais: Formatação de strings

# Comparacao de python 2 e python 3 para formatacao => https://pyformat.info

# Documentação => https://cursos.alura.com.br/course/python-3-introducao-a-nova-versao-da-linguagem/task/25640

print("Tentativa {} de {}".format(1, 3))


print("R$ {}".format(1.59))


# :f -> informar que é um tipo float
print("R$ {:f}".format(1.59))

#  formatar apos o ponto, duas casas decimais do valor
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:.2f}".format(1234.50))

#  informar o numero maximo de caractere neste caso
# 7 = (4 numeros, mais o ponto, mais duas casas decimais)
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))

# Se quisermos preencher os espaços em branco com zeros 0
print("R$ {:07.2f}".format(1.5))

# FORMATAÇÃO DE INTEIROS

# passamos a letra d
print("R$ {:07d}".format(4))

# formatando data
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))



