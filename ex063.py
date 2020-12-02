num = int(input('Informe um número: '))
cont = 1
termA, termB = 0, 1
soma = 0
print('{} -> {}'.format(termA, termB), end='')
while cont < num:
    termA, termB = termB, termB + termA
    print(' -> {}'.format(termB), end='')
    cont += 1
