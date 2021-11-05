#Leia o nome completo de uma pessoa
#Leia o primeiro nome separadamente
#Leia o segundo nome separademente
#Ex primeiro = ana segundo = silva
nome = str(input('Digite o seu nome completo')).strip()
separado = nome.split()
print('Prazer em te conhecer')
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu ultimo nome é {}'.format(separado[-1]))


