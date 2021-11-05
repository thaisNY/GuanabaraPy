#Melhore o desafio 28
#Faça o computador pensar num número de 0 a 10
#confira se você acertou
#Imprima qvas você precisa
import random
n1 = int(input('Pense num número de 0 a 10 e digite'))
lista = [1,2,3,4,5,6,7,8,9,10]
n2 = random.choice(lista)
if n1 == n2 :
    print('Parabéns você acertou de primeira')
else :
    print('Você errou o computador pensou no número {}'.format(n2))
condicao = (n1 != n2)
tentativas = 1
while (condicao):
    n1 = int(input('Tente novamente'))
    n2 = random.choice(lista)
    tentativas = tentativas + 1
    if n1 == n2 :
        print('Você acertou')
        print('Você precisou de {} tentativas para acertar'.format(tentativas))
        break
    else :
        print('Você errou o computador pensou no número {}'.format(n2))
