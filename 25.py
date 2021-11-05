#Crie um programa que leia o nome de uma pessoa
#Diha se ela tem Silva np nome
nome = str(input('Digite o seu nome ')).strip()
print('Seu nome tem silva ? {}'.format('silva' in nome.lower()))