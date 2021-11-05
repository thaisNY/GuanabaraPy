#Simule u caixa eletrónico com cédulas de 50,20,10 e 1
#Banco CEV
#Pergunte o valor que você quer sacar
#Total de {} cédulas de 50;Total de {} cedulas de 10 e Total de {}  cédulas de 1
print('='*20)
print('Banco cev')
print('='*20)
valor = int(input('Quanto você quer sacar ?'))
total = valor
céd = 50
totcéd = 0
while True :
    if total >= céd :
        total -= céd
        totcéd += 1
    else :
        print(f'O total de cédulas de {céd} foi de {totcéd}')
        if céd == 50 :
            céd = 20
        elif céd == 20 :
            céd = 10
        elif céd == 10 :
            céd = 1
        totcéd = 0
        if total == 0 :
            break