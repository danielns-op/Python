n = int(input('Informe um número inteiro: '))

print('Tabuada do {}'.format(n))
print('-' * 13)

for valor in range(1, 11):
    print('{} x {:2} = {}'.format(n, valor, n * valor))

print('-' * 13)
