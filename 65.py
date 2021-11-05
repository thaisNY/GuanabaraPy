#Leia números inteiros pelo teclado
#Mostre a média de todos os valores lidos
#Mostre o maior e o menor valor
#O programa deve perguntar ao usuario se ele quer continuar a digitar valores ou não
n = int(input('Digite um número inteiro:'))
i = 1
s = n
maior = n
menor = n
resp = str(input('Quer continuar a digitar sim ou não')).lower()
while (resp == 'sim') :
        n = int(input('Digite um número inteiro:'))
        resp = str(input('Quer continuar a digitar sim ou não')).lower()
        i = i + 1
        s = s + n
        media = (s)/(i)
        if n > maior :
            maior = n
        elif n < menor :
            menor = n
        print(s)
        print(i)
        print('A média entre os números é {}'.format(media))
        print('O maior é {} e o menor é {}'.format(maior,menor))




