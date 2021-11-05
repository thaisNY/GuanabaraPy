from time import sleep
def contador1():
    print('-='*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1,10 + 1,1):
        print(f'{c} ',end="" )
        sleep(0.5)
    print('FIM!')
    print('-=' * 30)
    print('Contagem de  10 até 0 de 2 em 2')
    for c in range(10,-1,-2):
        print(f'{c} ',end="" )
        sleep(0.5)
    print('FIM!')
    print('-=' * 30)
def contador2(inicio,fim,passo):
    print('Hora de personalizar a contagem!')
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    if passo > 0 :
        print()
        for c in range(inicio,fim + 1,passo):
            print(f'{c} ',end="")
            sleep(2)
        print('FIM!')
    else:
        for c in range(inicio,fim - 1,passo):
            print(f'{c} ', end="")
            sleep(2)
        print('FIM!')

#Programa principal
contador1()
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador2(inicio,fim,passo)

