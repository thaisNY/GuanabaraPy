jogador = dict()
jogador['nome'] = str(input('Nome do jogador?'))
jogador['num_partidas'] = int(input('Quantas patidas o jogador jogou?'))
num = jogador['num_partidas']
total = 0
gols = []
for i in range (0,num):
    gol = int(input('Numero de gols'))
    gols.append(gol)
    total += gol
jogador['gol_partida'] = gols
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
print('O campo nome tem valor '+ jogador['nome'])
print(f'O campo gols tem valor {gols}')
print(f'O campo total tem valor {total}')
print('-='*30)
mensagem = 'O jogador'+' '+jogador['nome']+' '+f'jogou {num} partidas.'
print(mensagem)
for c in range(0,len(gols)):
    print(f' => Na partida {c}, fez {gols[c]} gols')
print(f'Foi um toral de {total} gols')

