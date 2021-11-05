#Leia o peso de cinco pessoas
#Mostre o maior
#Mostre o menor
peso = float(input('Digite o seu peso'))
maior = peso
menor = peso
for c in range (4) :
    peso = float(input('Digite o seu peso :'))
    if peso > maior :
        maior = peso
    elif peso < menor :
        menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))