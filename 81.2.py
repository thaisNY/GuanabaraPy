valores = []
while True :
    valores.append(int(input('Digite um valor')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(valores)} valores na lista')
valores.sort(reverse=True)
print(f'Os valores em ordem descrencente são {valores}')
if 5 in valores :
    print('O valor 5 faz parte da lista!')
else :
    print('O valor 5 nao esta presente na lista')