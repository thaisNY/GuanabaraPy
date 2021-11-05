#Leia um número
#Imprima a tabuado dele usando um laço for
n = int(input('Digite um número'))
s = 1
print('-'*12)
for c in range (1,11) :
    print('{} x {} = {}'.format(n,s, n * s))
    s+=1
print('-'*12)