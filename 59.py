#Leia 2 números
#Mostre o menu : 1 somar , 2 multiplicar , 3 maior , 4 novos números , 5 sair do programa
n1 = int(input('Digite um número :'))
n2 = int(input('Digite um número :'))
print('-'*12)
print('Menu')
print('-'*12)
print('[1] soma    [2] multiplicação'
      ' [3] maior  [4] novos números'
      ' [5] sair')
opcao = int(input('Digite o valor correspondente a sua opção :'))
while (opcao < 6) :
    if opcao == 1 :
        soma = 0
        soma = n1 + n2
        print('A soma entre {} e {} é {} :'.format(n1,n2,soma))
        break
    elif opcao == 2 :
        multiplicar = 0
        multiplicar = n1 * n2
        print('A multiplocação entre {} e {} é {}:'.format(n1,n2,multiplicar))
        break
    elif opcao == 3 :
        if n1 > n2 :
            print('Entre {} e {} o maior é {}'.format(n1,n2,n1))
        elif n1 < n2 :
            print('Entre {} e {} o maior é {}'.format(n1,n2,n2))
        else :
            print('Os números são iguais não existe maior')
        break
    elif opcao == 4 :
        aux1 = 0
        aux2 = 0
        A = int(input('Digite um novo valor para n1'))
        B = int(input('Digite um novo valor para n2'))
        aux1 = n1
        n1 = A
        A = aux1
        aux2 = n2
        n2 = B
        B = aux2
        print('Os novos valores paras variáveis são {} e {}'.format(n1,n2))
        break

    elif opcao == 5 :
        break