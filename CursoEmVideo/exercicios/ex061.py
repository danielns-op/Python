ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = ptermo
print('Progressão Aritmética - PA')
print('do termo {} e razão {} é:'.format(ptermo, razao))
cont = 0
while cont < 9:
    print('{}, '.format(termos), end='')
    termos += razao
    cont += 1
print('{}.'.format(termos), end='')
