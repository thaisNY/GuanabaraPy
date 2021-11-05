#Leia um número n
#Imprima uma sequência de fibonacci até o n(enegissimo) termo
numrepeticoes = int(input('Digite o número de termos na sequência que você deseja ter :'))
a = 0
b = 1
i = 0
while (i < numrepeticoes) :
    i = i + 1
    aux = a + b
    a = b
    b = aux
    print(aux)

