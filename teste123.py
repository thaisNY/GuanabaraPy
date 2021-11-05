def contador2(incio,fim,passo):
    print('Hora de personalizar a contagem!')
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    if passo > 0 :
        print(passo)
        for c in range(inicio,fim + 1,passo):
            print(c)
        print('FIM!')
    else:
        for c in range(inicio,fim - 1,passo):
            print(c)
        print('FIM!')

#Programa principal

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador2(inicio,fim,passo)
