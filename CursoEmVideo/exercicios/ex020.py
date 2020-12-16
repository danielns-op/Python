from random import shuffle

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print('Ordem de apresentação:')

for i in alunos:
    print(i)
