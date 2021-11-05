#Leia uma frase
#Diga se ela é um polindromo ex A sacada da casa desconsidere espaços
frase = str(input('Digite uma frase'))
frase1 = frase.replace(' ','')
print(frase1)
tamanho = len(frase1)
print(tamanho)
frase1reverso = ''
frase1reverso = frase1[::-1]
print(frase1reverso)
if frase1 == frase1reverso :
    print('é um polindromo')
else :
    print('não é polindromo')
