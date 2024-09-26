# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = input("Digite a string a ser invertida: ")
reversa = []
palavra = list(palavra)

while palavra:
    ultima = palavra[-1]
    reversa.append(ultima)
    palavra.pop()


reversa = ''.join(reversa)
print(reversa)