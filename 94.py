cadastro = dict()
resp =""
tot = 0
sum = 0
media = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: '))
    if cadastro['sexo'] not in 'MmFf':
        print('Voce digitou um sexo invalido')
        continue
    cadastro['idade'] = float(input('Idade: '))
    resp = str(input('Quer continuar [S/N]'))
    tot += 1
    sum += cadastro['idade']
    if resp in 'Nn':
        break
media = 0
media = sum/tot
print(f' A) Ao todo temos {tot} pessoas cadastradas')
print(f'B)  A media da idade é {media} ')
for key in cadastro:
    if cadastro['sexo'] in 'Ff':
        print(f'c) As mulheres cadastradas foram {cadastro["nome"]} ')
for key in cadastro:
    if cadastro['idade'] > media:
        print(f'd) A lista de pessoas que ficou acima da media foi nome = {cadastro["nome"]}; sexo = {cadastro["sexo"]}; idade = {cadastro["idade"]}')

#não consegui imprimir as letra c e d
