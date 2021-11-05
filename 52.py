#Leia um número inteiro
#Diga se ele é primo
num = int(input('Digite um número inteiro'))
divisores = 0
for c in range(2,num,1) :
   if num % c == 0 :
        divisores = divisores + 1
        break
if divisores == 0 :
    print('É primo')
else :
    print('Não é primo')
