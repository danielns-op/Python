numeros = []
n_pares = []
n_impar = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        n_pares.append(num)
    else:
        n_impar.append(num)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(f'Lista gerada: {numeros}')
print(f'Lista par: {n_pares}')
print(f'Lista ímpar: {n_impar}')
