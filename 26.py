#Leia a frase pelo teclado
#Quantas vezes aparece a letra a
#Em que posição aparece pela primeira vez
#Em que posição aparece pela última vez
frase = str(input('Digite uma frase')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeria posição que aparece a letra A é {}'.format(frase.find('A')+1))
print('A ultima posição que aparece a letra A é {} '.format(frase.rfind('A')+1))
