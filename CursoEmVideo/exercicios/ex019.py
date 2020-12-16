from random import randint

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

# P° Gustavo utilizou a função 'choice' na biblioteca math
sort = randint(0, 3)

print('O aluno(a) {} irá apagar o quadro'.format(alunos[sort]))
