#Leia vários números interiros
#O programa parar quando o usúario digitar 999
#Mostre quantos números foram digitados
#Mostre a soma entre eles
n = int(input('Digite um valor inteiro:'))
i = 0
s = n
while (n != 999) :
    n = int(input('Digite um valor inteiro:'))
    i = i + 1
    s = s + n
print('Foram digitados {} números'.format(i))
print('A soma entre os números é : {}'.format(s - 999))

