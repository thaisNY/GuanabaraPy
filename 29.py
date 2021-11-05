vel = int(input('Qual a velociade do seu carro?'))
if vel > 80 :
    print('Você vai pagar uma multa de {} reais'.format(((vel - 80)*7)))