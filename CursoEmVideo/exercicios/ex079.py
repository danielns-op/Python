numeros = []

while True:
    numero = int(input('Informe um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Número adicionado com sucesso.')
    else:
        print('Valor duplicado, o mesmo não será adicionado.')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Você adicionou os números: {sorted(numeros)}')
