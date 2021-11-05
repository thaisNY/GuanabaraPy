#Mostre quantos números o usuario digitou
#Mostre a lista de números em ordem decrescente
#Cheque se 5 está na lista
numeros = list()
resposta =""
cout = 0
while True :
    n = int(input('Digite um número '))
    resposta = str(input('Quer continuar ?'))
    if resposta in 'Ss' :
        numeros.append(n)
        cout += 1
        numeros.sort(reverse=True)
        if n == 5 in numeros:
            print('O números 5 está na lista')
        print(numeros)
        print(f'Foram digitados {cout} numeros')
    elif resposta in 'Nn' :
        break
