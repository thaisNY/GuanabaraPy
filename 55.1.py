vetor = [0] * 5
for c in range (5) :
    vetor [c] = float(input('Digite um valor :'))
maior = vetor[0]
menor = vetor[0]

for c in range (1,5) :
    if vetor[c] > maior :
        maior = vetor[c]
    elif vetor[c] < menor :
        menor = vetor[c]
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))