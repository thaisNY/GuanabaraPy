#Leia o nome da aluna , a sua primeira nota e a sua segunda nota,pergunte se quer continuar  se sim continue lendo
#imprima um tabela com o número do aluno,nome e media
#Mostrar as notas de qual aluno ? Decidir pelo número e imprimir as notas de fulano foram (nota1,nota2)
#999 interompe o laço
media = 0
medias = []
alunos = []
notas = []
cont = 0
while True :
    aluno = str(input('Digite o nome do aluno :'))
    nota1 = int(input('primeira nota :'))
    nota2 = int(input('segunda nota :'))
    resp = str(input('Quer continuar ? (s/n)'))
    media = (nota1 + nota2)//2
    cont += 1
    medias.append(media)
    alunos.append(aluno)
    notas.append(nota1)
    notas.append(nota2)
    if resp  in 'Nn' :
        break
print('-='*30)
print('-'*30)
print('No     Nome     Média')
for c in range (cont) :
    print(f'{c}       {alunos[c]}       {medias[c]}')
print('-'*30)
while True :
    resp = int(input('Mostrar a nota de qual aluno ?(999 interrompe)'))
    if resp == 0 :
        print(f'Notas de {alunos[resp]} são {notas[0]} e {notas[1]}')
    elif resp != 0 and resp != 999 :
        print(f'Notas de {alunos[resp]} são {notas[2*resp]} e {notas[ (2*resp) + 1]}')
    elif  resp == 999 :
        break






