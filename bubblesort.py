lista = [35,21,12,67,14,89]
ordenado = False
while not ordenado:
    ordenado = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            ordenado = False
            lista[i + 1], lista[i] = lista[i], lista[i + 1]
            print(lista)

print(lista)
#Algoritimo de bubble sort worst case o (n) ^ 2