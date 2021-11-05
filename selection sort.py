lista = [7,1,13,89,51,10]
for i in range (len(lista) ):
    menor = i
    for j in range(i + 1, len(lista)):
        if lista[menor] > lista[j]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
print(lista)
#selection sort worst case o(n) ^ 2