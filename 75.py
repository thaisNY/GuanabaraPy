#Leia 4 valores pelo teclado
#Guardeos numa trupla
#Mostre quantas vezes apareceu o valor 9
#Mostre em que posição foi degitado o valor 3
#Quais foram os valores pares
lista = []
print('Degite 4 valores')
for i in range (4) :
    num = int(input())
    lista.append(num)
print(lista)
print(f'O valor 9 apareceu {lista.count(9)} vezes')
print(f'O primeiro 3 está na posição {lista.index(3)}')
lista2 = []
for valor in lista:
    if valor % 2 == 0:
        lista2.append(valor)
print('Os números pares da trupla são {}'.format(lista2))