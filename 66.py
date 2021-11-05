#Leia vários números inteiros
#O programa vai parar quando você degitar 999
#Imprima quantos números foram degitados e a soma entre eles
#Ex a soma de {} números foi de {}
i = s = 0
n = int(input('Digite um número :'))
while (n != 999) :
    i = i + 1
    s += n
    n = int(input('Digite um número novamente:'))
print(f'A soma de {i} números foi {s}')


