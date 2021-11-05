#Leia o ano de nascimento
#Calcule a sua idade
#Mostre a categoria
# Até 9 anos mirim
#Até 14 anos infantil
#Até 19 anos junior
#Até 20 anos senior
#Acima Master
ano = int(input('Digite o ano do seu nascimento'))
idade = 2020 - ano
print('A sua idade é {}'.format(idade))
if idade <= 9 :
    print('Mirim')
elif 9 < idade <= 14 :
    print('Infantil')
elif 14 < idade <= 19 :
    print('Junior')
elif 19 < idade <= 20 :
    print('Senior')
else :
    print('Master')