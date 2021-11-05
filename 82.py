#Leia os números digitados pelo usuario
#imprima a lista de numeros,imprima os pares e os impares
numeros = list()
pares = list()
impares = list()
while True :
    n = int(input('Digite um número :'))
    resp = str(input('Quer continuar ?'))
    if resp in 'Nn' :
        break
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else :
        impares.append(n)
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros impares é {impares}')
print(f'a lista de numeros que você digitou foi {numeros}')
