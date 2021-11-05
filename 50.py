#Leia 6 números
#Mostre a soma dos 6 números
#Mostre a soma apenas dos que forem pares
n = 0
s = 0
for c in range (1,7) :
    n =int(input('Digite um número'))
    if n % 2 == 0 :
        s += n
print('A soma dos números é {}'.format(s))
