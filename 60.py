#Leia um número qualquer
#Mostre o seu fatorial
resp = 1
c = 1
n = int(input('Digite um número :'))
while (c < n) :
    c = c + 1
    resp = resp * c
print('O fatorial de {} é {}'.format(n,resp))