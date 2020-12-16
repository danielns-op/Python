numeros = []
for n in range(1, 6):
    numeros.append(int(input(f'Informe o {n}º número: ')))

maior = max(numeros)
menor = min(numeros)

print('-=' * 26)

print(f'Números informados: {numeros}')

if numeros.count(maior) > 1:
    print(f'O maior número é {maior} e está nas posições:', end='')
    for pos, num in enumerate(numeros):
        if num == maior:
            print(f' {pos}... ', end='')
    print('')
else:
    print(f'O maior número é {maior} e está na posição: {numeros.index(maior)}')

if numeros.count(menor) > 1:
    print(f'O menor número é {menor} e está nas posições:', end='')
    for pos, num in enumerate(numeros):
        if num == menor:
            print(f' {pos}... ', end='')
    print('')
else:
    print(f'O menor número é {menor} e está na posição: {numeros.index(menor)}')

print('=-' * 26)
