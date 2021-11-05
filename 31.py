dis = int(input('Quantos kms tem a viagem?'))
if dis <= 200 :
    print('O valor da passagem a ser pago é {}'.format(dis*0.5))
else :
    print('O valor da passagem a ser pago é {}'.format(dis*0.45))
