#Leia peso e altura
#Calcule o IMC
#Mostre seu staatus sendo 18.5 abaixo do pes0 , entre 18.5 e 25 peso ideal , entre 30 e 40 obesidade , acima de 40 obesidade mórbida
peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso/(altura * altura)
if imc <= 18.5 :
    print('Você está abaixo do peso')
elif 18.5 < imc <= 25 :
    print('Você está no peso ideal')
elif 25 < imc <= 30 :
    print('Você está com sobre peso')
elif 30 < imc <= 40 :
    print('Você está obeso')
else :
    print('Você está com obsidade mórbida')
