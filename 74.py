#Gere 5 números aleatorios
#Imprima eles
#Imprima o maior
#Imprima o menor
import random
lista = [0,1,2,3,4,5,6,7,8,9]
lista2 = []
maior = -1
menor = 10
for c in range (1,6,1) :
    sorteado = random.choice(lista)
    lista2.append(sorteado)
print(lista2)
for valor in lista2 :
    if valor > maior:
        maior = valor
    if valor < menor :
        menor = valor
print(f'O maior valor da lista é {maior}')
print(f'O menor valor da lista é {menor}')
