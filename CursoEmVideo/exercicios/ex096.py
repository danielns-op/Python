# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terro retangular (largura e comprimento)
# e mostre a área do terreno.

def area(l, c):
    areat = l * c
    print(f'A Área de um terreno {l}x{c} é: {areat:.1f}m²\n')


print('Controle de Terrenos')
print('-' * 22)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)

