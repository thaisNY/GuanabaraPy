#Pergunte o valor da casa
#Pergunte o salario do comprador
#Pergunte em quantos anos ele vai pagar
#Calcule a prestação sabendo que ela n pode ser + que 30% do que o salario
v_casa = float(input('Digite o valor da casa'))
salario = float(input('Digite o valor do salario'))
anos = int(input('Quantos anos você pretende pagar a casa'))
prestacao = v_casa/(anos*12)
if prestacao > salario*0.3 :
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aprovado')
    print('O valor da prestação é {}'.format(prestacao))
