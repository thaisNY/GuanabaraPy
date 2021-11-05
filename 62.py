#Melhore o desafio 61
#Pergunte se o usario quer mostrar mais termos
#O programa encerra quando o usúario disser que quer mostrar 0 termos
a1 = int(input('Digite o primeiro termo da Pa'))
r = int(input('Digite a razão da Pa'))
termo = 0
cont = 0
condicao = True
while (condicao) :
    continuar = str(input('Você quer mostrar mais 1 termo sim ou não')).lower()
    if continuar == 'sim' :
        termo = a1 + (cont * r)
        cont = cont + 1
        print(termo)
    else :
        print('Fim do programa')
        break

