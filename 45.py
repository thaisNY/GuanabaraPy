import random
pessoa = str(input('Escolha entre papel,pedra e tesoura'))
lista = ['papel','pedra','tesoura']
computador = random.choice(lista)
print('Você escolheu {} e o computador escolheu {}'.format(pessoa,computador))
if pessoa == computador :
    print('Empate,jogue novamente')
elif pessoa == 'papel' and computador == 'pedra' :
    print('Você ganhou')
elif pessoa == 'papel' and computador == 'tesoura' :
    print('Você perdeu')
elif pessoa == 'pedra' and computador == 'tesoura' :
    print('Você ganhou')
elif pessoa =='pedra' and computador == 'papel' :
    print('Você perdeu')
elif pessoa == 'tesoura' and computador == 'papel' :
    print('Você ganhou')
elif pessoa == 'tesoura' and computador == 'pedra' :
    print('Você perdeu')


