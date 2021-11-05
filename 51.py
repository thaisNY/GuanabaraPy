#Leia o primeiro termo de uma pa
#Leia a razão da pa
#Imprima os 10 primeiros termos da pa
a1 = int(input('Digite o primeiro termo da Pa'))
r = int(input('Digite a razão da Pa'))
termo = 0
cont = 0
for c in range (a1,11):
    termo = a1 + (cont*r)
    print(termo)
    cont = cont + 1



