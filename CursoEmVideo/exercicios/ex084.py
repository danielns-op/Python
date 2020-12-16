# Faça um programa que leia nome e peso de várias
# pessoas, guardando tudo em uma lista. No final,
# mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves.

lista = []
mais_pesado = []
mais_leve = []
pesado = leve = contador = 0

while True:
    dados = list()
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    contador += 1
    if contador == 1:
        pesado = dados[1]
        mais_pesado.append(dados[:])
        leve = dados[1]
        mais_leve.append(dados[:])
    else:
        if dados[1] > pesado:
            mais_pesado.clear()
            pesado = dados[1]
            mais_pesado.append(dados[:])
        if dados[1] == pesado:
            if dados[:] not in mais_pesado:
                mais_pesado.append(dados[:])
        if dados[1] < leve:
            mais_leve.clear()
            leve = dados[1]
            mais_leve.append(dados[:])
        if dados[1] == leve:
            if dados[:] not in mais_leve:
                mais_leve.append(dados[:])
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print('=-' * 15)
print(f'Ao todo você cadastrou {len(lista):.0f} pessoas.')

print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for pos in range(0, len(mais_pesado)):
    print(f'[{mais_pesado[pos][0]}] ', end='')
print('')
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')
for pos in range(0, len(mais_leve)):
    print(f'[{mais_leve[pos][0]}] ', end='')
print('')
print('-=' * 15)
