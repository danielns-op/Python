print('Soma dos números:')

soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
print('''
A soma de todos os números ímpares
que são múltiplos de três e que se
encontram no intervalo de 1 até 500 é {}.'''.format(soma))
