#Leia um número
#Escolha se você quer par ou ímpar
#Faça o computador escolher um número
#Some o n_humano e n _pc
#Decida se é par ou ímpar
#Se você conseguiu adivinhar [P/I] e avalie se você ganhou ou perdeu
#Se você perdeu : Game over você venceu {} vezes
#Se você ganhou Jogue novamente
import random
n_humano = int(input('Digite um número:'))
p_humano = str(input('Par ou impar'))
lista = [1,2,3,4,5,6,7,8,9,10]
n_pc = random.choice(lista)
print(f'O computador escolheu o número {n_pc}')
sum = 0
sum = n_humano + n_pc
print(f'A soma entre os números foi {sum}')
p_resultado = ''
vitoria = 0
while (vitoria >= 0) :
    if sum % 2 == 0 :
        p_resultado = 'par'
        print('O número é par')
    else :
        p_resultado = 'impar'
        print('o número é impar')
    if p_resultado == p_humano :
        vitoria = vitoria + 1
        print('Você venceu')
        print('Jogue novamente')
        import random

        n_humano = int(input('Digite um número:'))
        p_humano = str(input('Par ou impar'))
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n_pc = random.choice(lista)
        print(f'O computador escolheu o número {n_pc}')
        sum = 0
        sum = n_humano + n_pc
        print(f'A soma entre os números foi {sum}')
        p_resultado = ''
        if sum % 2 == 0:
            p_resultado = 'par'
            print('O número é par')
        else:
            p_resultado = 'impar'
            print('o número é impar')
        if p_resultado == p_humano:
            vitoria = vitoria + 1
            print('Você venceu')
            print('Jogue novamente')
    else :
        print(f'Game over você venceu {vitoria} vez(es)')
        break





