lista = []
mais_pesado = []
mais_leve = []

while True:
    dados = list()
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if dados[1] >= 100:
        mais_pesado.append(dados)
    if dados[1] <= 70:
        mais_leve.append(dados)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print('=-' * 15)
print(f'Ao todo você cadastrou {len(lista):.0f} pessoas.')

pesado = 0
leve = 0

for info in mais_pesado:
    if info[1] > pesado:
        pesado = info[1]
print(f'O maior peso foi de {pesado}Kg. ', end='')
print('Peso de ', end='')
for info in mais_pesado:
    if info[1] == pesado:
        print(f'[{info[0]}] ', end='')
print('')

for info in mais_leve:
    if mais_leve.index(info) == 0:
        leve = info[1]
    else:
        if info[1] < leve:
            leve = info[1]
print(f'O menor peso foi de {leve}Kg. ', end='')
print('Peso de ', end='')
for info in mais_leve:
    if info[1] == leve:
        print(f'[{info[0]}] ', end='')
print('')
print('-=' * 15)
