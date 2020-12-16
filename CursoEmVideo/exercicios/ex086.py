# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.

matriz = [[], [], []]

for pos in range(0, len(matriz)):
    for valor in range(0, len(matriz)):
        matriz[pos].append(int(input(f'Informe um número para a posição [{pos}, {valor}] número: ')))

print('-=' * 15)

for pos in range(0, len(matriz)):
    for valor in matriz[pos]:
        print(f'[ {valor:^5} ]', end='')
    print('')
