#Leia a idade de várias pessoas
#Leia o sexo de várias pessoas
#Pergunte se você quer continuar ou não
#Se sim volta para o loop
#Se não :
#Imrima : quantas pessoas tem mais de 18 anos
#Quantos homems foram cadastrados
#Quantas mulheres tem menos de 20 anos

mais_18 = 0
n_homens = 0
mulher_menos20 = 0


idade = int(input('Digite a sua idade:'))
sexo = str(input('Digite o seu sexo femenino ou masculino')).lower()
continuar = str(input('Você quer continuar sim ou não ?')).lower()

if idade > 18:
    mais_18 = 1

if sexo == 'masculino' and idade > 0:
    n_homens = 1

if sexo == 'femenino' and idade < 20:
    mulher_menos20 = 1

while (continuar == 'sim') :
    idade = int(input('Degite a sua idade:'))
    sexo = str(input('Degite o seu sexo masculino ou femenino')).lower()
    continuar = str(input('Você quer continuar sim ou não ?')).lower()
    if idade > 18 :
        mais_18 = mais_18 + 1

    if sexo == 'masculino' and idade > 0 :
        n_homens = n_homens + 1

    if sexo == 'femenino' and idade < 20 :
        mulher_menos20 = mulher_menos20 + 1

print(f'Tem {mais_18} pessoa(s) com mais de 18 ano(s)')
print(f'O total de homem(s) é de {n_homens}')
print(f'Existem {mulher_menos20} mulheres com menos de 20 anos')

