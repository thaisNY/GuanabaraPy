#Crie um programa que pergunte ao usuario quantos jogos ele quer sortiar e imprima jogos da mega sena mas,n pode repetir
# o mesmo numero
import random
print('-='*30)
print('Jogo na Mega Sena')
print('-='*30)
count = int(input('Quantas vezes você quer que eu sortei?'))
print('-=-=-= Sorteando 10 jogos -=-=-=-')
a = b = c = d = e = f = 0
jogo = [a,b,c,d,e,f]
for i in range (1,count + 1) :
    a = random.choice(range(1, 60))
    b = random.choice(range(1, 60))
    c = random.choice(range(1, 60))
    d = random.choice(range(1, 60))
    e = random.choice(range(1, 60))
    f = random.choice(range(1, 60))
    print(f'Jogo {i} : [{a},{b},{c},{d},{e},{f}]')
