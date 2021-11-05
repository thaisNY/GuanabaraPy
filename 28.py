import random
n1 = int(input('Chute um número entre 0 e 5'))
lista = [1,2,3,4,5]
n2 = random.choice(lista)
print('O numero sorteado foi {}'.format(n2))
if  n1 == n2 :
    print('Venceu')
else :
    print('Perdeu')
