# Aprimore o desafio anterior (ex086), mostrando no final:
#   A) A soma de todos os valores digitados.
#   B) A soma dos valores da terceira coluna.
#   C) O maior valor da segunda linha.

matriz = [[], [], []]
soma_par = 0

for pos in range(0, len(matriz)):
    for valor in range(0, len(matriz)):
        num = int(input(f'Informe um número para a posição [{pos}, {valor}] número: '))
        matriz[pos].append(num)
        if num % 2 == 0:
            soma_par += num

print('-=' * 15)

for pos in range(0, len(matriz)):
    for valor in matriz[pos]:
        print(f'[{valor:^5}]', end='')
    print('')

print(f'\nA Soma de todos os valores pares digitados é: {soma_par}')
print(f'A Soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
