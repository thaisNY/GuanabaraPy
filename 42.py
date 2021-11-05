#Leia os três lados de um triângulo
#Imprima se pode ou não formar um triângulo
#Imprima se ele é equilatero,isceles ou escaleno
a = float(input('Digite o valor para o lado de um triângulo'))
b = float(input('Digite o valor para um lado do triângulo'))
c = float(input('Digite o valor para um lado do triângulo'))
if a < b + c and b < a + c and c < a + b :
    print('Forma um triângulo')
    if a == b == c:
        print('O tirângulo é equilátero')
    elif a == b or a == c or b == c:
        print('O triângulo é isóceles')
    else:
        print('O triângulo é escaleno')
else :
    print('Não forma um triângulo')
