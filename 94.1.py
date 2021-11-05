galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear() #clear para n mudar o dicionario original
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy()) #adicionando um dicionario a uma lista
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO Responda apenas S  ou N')
    if resp == 'N':
        break
print('*'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma/len(galera)
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f}')
print(f'As mulheres cadastradas foram', end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end = '')
print()
for p in galera: # para cada pessoa em galera se a chave idade for..., percorrendo cada dict dentro da lista
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}', end='') #k keys v values em items
        print()
print('<<<ENCERADO>>>')

