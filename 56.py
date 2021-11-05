#Leia nome,idade e sexo de 4 pessoas
#Imprima a média de idade do grupo
#Imprima o nome do homem mais velho
#Quantas mulheres tem menos de 20
soma = 0
maisvelho = 0
nome_velho = ''
mulheres_menor20 = 0
for p in range (1,5) :
    nome = str(input('Digite o seu nome :')).strip()
    sexo = str(input('Digite o seu sexo m para homens e f para mulheres:')).strip()
    idade = int(input('Digite a sua idade:'))
    soma = soma + idade
    if p == 1 and sexo == 'm':
        maisvelho = idade
    if sexo == 'm' and idade > maisvelho :
        maisvelho = idade
        nome_velho = nome
    if sexo == 'f' and idade < 20 :
        mulheres_menor20 +=1

media = soma / 4
print('A média de idade  do grupo de pessoas é {}'.format(media))
print('O nome do homem mais velho é {}'.format(nome_velho))
print('Tem {} mulheres menores de 20 anos'.format(mulheres_menor20))





