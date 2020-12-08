lista = [[], []]

for v in range(1, 8):
    num = int(input(f'Informe o {v}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')
