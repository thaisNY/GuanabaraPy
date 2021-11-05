#Leia a idade de 7 pessoas
#Diga quatas são maiores de idade
#Quantas não são
maiores_idade = 0
menores_idade = 0
for c in range (1,8,1) :
    idade = int(input('Digite a sua idade'))
    if idade >= 18 :
        maiores_idade = maiores_idade + 1
    else :
        menores_idade = menores_idade + 1
print('Tem {} pessoas maiores de idade'.format(maiores_idade))
print('Tem {} pessoas menores de idade'.format(menores_idade))




