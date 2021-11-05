#Refaça o desafio 51
#Leia o primeiro termo e a razão de uma Pa
#Imprima os 10 primeiros termos
a1 = int(input('Digite o primeiro termo da Pa'))
r = int(input('Digite a razão da Pa'))
termo = 0
cont = 0
while (cont < 10) :
    termo = a1 + (cont * r)
    cont = cont + 1
    print(termo)

