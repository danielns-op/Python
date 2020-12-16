escolha = int(input('Qual tabuada gostaria de ver [1 a 10]: '))
print('{:-^30}'.format('Tabuada do número {}'.format(escolha)))
for c in range(1, 11):
    valor = escolha * c
    print('{:^30}'.format('{} X {:<2} = {:<2}'.format(escolha, c, valor)))
print('-' * 30)
