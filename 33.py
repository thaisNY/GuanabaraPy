n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))
n3 = int(input('Digite um número'))
if n1 > n2 and n1 > n3 :
    print('o maior é {}'.format(n1))
elif n2 > n1 and n2 > n3 :
    print('o maior é {}'.format(n2))
else :
    print('o maior é {}'.format(n3))
if n1 < n2 and n1 < n3 :
    print('o menor é {}'.format(n1))
elif n2 < n1 and n2 < n3 :
    print('o menor é {}'.format(n2))
else :
    print('o moner é {}'.format(n3))

