produtos = ('Caderno', 15, 'Estojo', 8, 'caneta', 1.5, 'Mochila', 80,
            'Lapís', 0.5, 'Borracha', 1.5, 'Livro A', 33.6, 'livro B',
            37.9, 'Cola', 7, 'Apontador', 1)

print('-=' * 15)
print('{:^30}'.format('Lista dos Produtos'))
print('=-' * 15)
for valor in range(0, len(produtos)):
    if valor % 2 == 0:
        print(f'{produtos[valor]:.<20} ', end='')
    else:
        print(f'R$ {produtos[valor]:^6.2f}')
print('-=' * 15)
