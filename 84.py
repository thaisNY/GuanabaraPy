#Faça um programa que leia nome e peso de várias pessoas guardando em uma lista e imprima quantas pessoas foram
#adicionadas a listagem de pessoas mais pesadas e a listagem das pessoas mais leves
temp = []
princ = []
mai = men = 0
while True :
    temp.append(str(input('Nome :')))
    temp.append(float(input('Peso :')))
    if len(princ) == 0:
        mai = men = temp[1]
    else :
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men :
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar ? [s/n]'))
    if resp in 'Nn' :
        break
print('-='*30)
print(f'Ao todo voce cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg Peso de',end = '')
for p in princ :
    if p[1] == mai :
        print(f'{p[0]}',end = '')
print(f'O menor peso foi de {men}kg.Peso de', end = '')