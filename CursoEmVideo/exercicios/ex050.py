soma = 0
for c in range(0, 6):
    num = int(input('Informe o número {}:'.format(c + 1)))
    if num % 2 == 0:
        soma += num
print('''Você informou 6 números, desses
a soma dos números pares é {}.'''.format(soma))
