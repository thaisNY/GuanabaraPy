#Leia um número
#Imprima a tabuada desse número
#Se o usuario digitar um número negativo encerre o programa
n = int(input('Você quer saber a tabuada de qual número ?'))
print('='*20)
j = 0
while (n > 0) :
    j = j + 1
    i = 0
    while (i < 10) :
        i = i + 1
        print(f'{n} x {i} = {n*i}')
    n = int(input('Você quer saber a tabuada de qual número ?'))
    print('Tabuada encerrada volte sempre')
print('='*20)
