preço = float(input('Digite o preço do produto'))
pagamento = str(input('Como você vai pagar ? Especie , cheque , cartão , cartão2x , cartão3x ou mais'))
if pagamento == 'especie' or pagamento == 'cheque':
      print('Você irá pagar {}'.format(preço - (preço*0.1)))
elif pagamento == 'cartão' :
      print('Você irá pagar {}'.format(preço - (preço*0.05)))
elif pagamento == 'cartão2x' :
      print('Você irá pagar {}'.format(preço))
elif pagamento == 'cartão3x' :
      print('Você irá pagar {}'.format(preço + (preço*0.2)))
