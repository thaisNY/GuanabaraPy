listanum =[]
maior = 0
menor = 0
for c in range (0,5) :
    listanum.append(int(input(f'Digite um valor para posção {c}')))
    if c == 0:
        maior=menor=0
    else :
        if listanum[c] > maior :
            maior = listanum[c]
        if listanum[c] < menor :
            menor = listanum[c]
for i, v in enumerate(listanum) :
    if v == maior :
        print(f'{i}...',end='')
print()
print(f'o maior é o número {maior} na ´posição {i}')
for i, v in enumerate(listanum) :
    if v == menor :
        print(f'{i}...',end='')
print()
print(f'o menor é o número {menor} na ´posição {i}')