l1 = float(input('Digite o valor de l1'))
l2 = float(input('Digite o valor de l2'))
l3 = float(input('Digite o valor de l3'))
if l2 - l3 < l1  < l2 + l3 and l1 - l3 < l2 < l1 + l3 and l1 - l2 < l3 < l1 + l2 :
    print('Forma um triangulo')
else :
    print('Não forma um triangulo')

