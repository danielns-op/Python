numeros = []
quant_num = cont = 0

while True:
    numero = int(input('Informe um número: '))
    numeros.append(numero)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Foram digitados {cont} números.')
print(f'Lista ordenada de forma decrescente: {sorted(numeros, reverse=True)}')
print(f'O número 5 está na lista') if 5 in numeros else print('O número 5 não está na lista.')
