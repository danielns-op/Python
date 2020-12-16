from time import sleep
print('*- Calculando Fatorial -*')
sleep(1)
num = int(input('Informe um número: '))
print('Opção com while:')
valor = num
fator = 1
print('{}! = '.format(num), end='')
while valor != 1:
    fator *= valor
    print('{}x'.format(valor), end='')
    valor -= 1
print('{} = {}'.format(valor, fator), end='')

print('\n\nOpção com for: ')
val = num
fat = 1
print('{}! = '.format(num), end='')
for i in range(num - 1):
    fat *= val
    print('{}x'.format(val), end='')
    val -= 1
print('{} = {}'.format(val, fat), end='')
