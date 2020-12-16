soma = 0
cont = 0
while True:
    num = int(input('Informe um número [999 - para]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Você digitou {} números.'.format(cont))
print('A soma desses números é: {}'.format(soma))
