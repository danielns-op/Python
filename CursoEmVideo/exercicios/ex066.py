cont = soma = 0

while True:
    num = int(input('Informe um número [999 - para]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma desses números é {soma}.')
