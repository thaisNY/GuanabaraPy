#Leia Nome : , e media :, -Imprima o nome é igual a João, - a media é igial a ,situação é igual a rec ou aprovado e rep
#Faça um programa que leia nome e média de um aluno,guardando a situação em um dicionario.No final, mostre o conteúdo na
#estrutura da tela
escola  = dict()
nome = str(input('Digite o nome do aluno'))
media = int(input('Digite a media do aluno'))
situacao = ''
if media >= 7 :
    situacao = 'aprovado'
elif media < 7 and media > 3 :
    situacao = 'recuperacao'
else :
    situacao = 'reprovado'

escola ['aluno'] = nome
escola ['media_geral'] = media
escola ['situacao_geral'] = situacao
print('-='*30)
print(escola)
