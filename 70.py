#Loja super baratão
#Leia o nome
#Leia o preço de vários produtos
#Você vai continuar ? S ou não
#Se sim volta para o loop
#Se não Imprima :
#Total de gasto
#Quantos custam mais de 1000
#O nome do produto mais barato

print('='*20)
print('SUPER BARATÃO')
print('='*20)

t_gasto = 0
i_mais1000 = 0
mais_barato = 90000000000000000
nome_maisbarato = ''
produto = ''
preço = 0
continuar = ''

produto = str(input('Nome do produto :')).upper()
preço = int(input('Preço :'))
continuar = str(input('Quer continuar [S/N] :')).upper()

t_gasto = preço
if preço > 1000 :
    i_mais1000 = 1

if preço < mais_barato :
    mais_barato = preço
    nome_maisbarato = produto

while (continuar == 'S') :
    produto = str(input('Nome do produto :')).upper()
    preço = int(input('Preço :'))
    continuar = str(input('Quer continuar [S/N] :')).upper()
    t_gasto += preço
    if preço > 1000 :
        i_mais1000 = i_mais1000 + 1
    if preço < mais_barato :
        mais_barato = preço
        nome_maisbarato = produto

print(f'O produto mais barato custa {mais_barato} e é o {produto}')
print(f'O total pago na conta foi de {t_gasto} reais')
print(f'Existem {i_mais1000} produto(s) que custam mais de mil reais')



