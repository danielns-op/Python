# Faça um programa que leia um número
# inteiro e diga se ele é ou não um
# número primo.

num = int(input('Informe um número: '))
cont = 0
for c in range(1, (num + 1)):
    if num % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')

if cont > 2:
    print('''\nO número {} foi divisível {} vezes,
    e por isso ele não é primo.'''.format(num, cont))
else:
    print('\nO número {} é PRIMO!'.format(num))
