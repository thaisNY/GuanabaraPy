#Leia o nome completo
#Imprima o nome completo maiscula
#Imprima o nome completo minusculo
#Imprima quantas letras tem o nome sem considerar os espaços
#Imprima quantas letras tem o primeiro nome
nome = str(input('Digite o seu nome completo'))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
primeiro = nome.split()
print(len(primeiro[0]))
