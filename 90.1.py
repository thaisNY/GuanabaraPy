#Faça um programa que leia nome e média de um aluno, guardando tambpem a situação em um dicinpario.No fonal mostre
#o conteúdo da estrutura na tela
#Dentro de aspas simples sempre use aspas duplas
aluno = dict()
aluno['nome'] = str(input('Nome :'))
aluno['media'] = float(input(f'Média de {aluno["nome"]} : '))
if aluno ['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 :
    aluno['situação'] = 'Recuperação'
else :
    aluno['situação'] = 'Reprovado'
# para imprimir de formatado
for k, v in aluno.items() :
    print(f'{k} é igual a  {v}')
