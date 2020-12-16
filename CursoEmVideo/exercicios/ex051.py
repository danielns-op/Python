ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = ptermo
print('Progressão Aritmética - PA')
print('do termo {} e razão {}'.format(ptermo, razao))

for c in range(1, 10):
    print('{}, '.format(termos), end='')
    termos += razao
print(termos)
