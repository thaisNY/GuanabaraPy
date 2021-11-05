#Leia o ano de nascimentos
#Confira se ele tem 18 mais ou menos,se menos vai,se mais passou  da hora,se igual deve se alistar
#Diga quanto tempo falta ou já passou do alistamento
ano = int(input('Diga o ano que você nasceu'))
idade = 2020 - ano
if idade < 18 :
    print('Você irá se alistar')
    falta = 18 - idade
    print('Falta {} anos para você'.format(falta))
elif idade > 18 :
    print('Você passou da idade de se alistar')
    passou = idade - 18
    print('Já passou {} anos que você deveria ter se alistado'.format(passou))
else :
    print('Você deve se alistar esse ano')

