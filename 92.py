#Leia o nome, ano de nascimento e caso a pessoa n tenha carteira, digite 0,caso tenha digite o numero da carteira
#o ano de contrataçao e o salario.Imprima o nome,a idade,a ctps,o ano de contratação,o salário e o ano da aposentadoria
#crie um programa que leia (nome,ano de nascimento e carteira de trabalho) e cadastre-os (com idade) em um dicionário
#receberá também  o ano de contratação e o salário.Calcule e acrescente ,além da idade, com quantos anos a pessoa vai se
# aposentar
#eh um dicionario variavel
trabalho = dict()
trabalho['nome'] = str(input('Digite seu nome: '))
trabalho['ano_nasc'] = int(input('Digite o ano de nascimento'))
trabalho['num_carteira'] = int(input('Digite o numero da cateira'))

if tabalho['num_carteira'] == 0 :

    print(f'O none tem valor {trabalho['nome']}')
    print(f'A idade tem valor {2021  - trabalho['ano_nasc']}')
    print(f'Os ctps tem valor {trabalho['num_carteira']}')

else:
    trabalho['ano_contratado'] = int(input('Digite o ano que voce foi contratado'))
    trabalo['salario'] = int(input('Digite o seu salario'))
    print(f'O none tem valor {trabalho['nome']}')
    print(f'A idade tem valor {2021  - trabalho['ano_nasc']}')
    print(f'Os ctps tem valor {trabalho['num_carteira']}')
    print(f'o ano de contratação tem valor {trabalho['ano_contratado']}')
    print(f'O ano de aposentadoria tem valor { 35 + trabalho['ano_contratado']}')
    
    