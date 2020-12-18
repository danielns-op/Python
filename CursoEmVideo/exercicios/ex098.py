#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que tenha uma função chamada contador(),
# que recebe três parâmetros: início, fim e passo e realize
# a contagem.
# Seu programa tem que realizar três contagens através da
# função criada:
#   A) De 1 até 10, de 1 em 1.
#   B) De 10 até 0, de 2 em 2.
#   C) Uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    print('-' * 45)
    print(f'Contagem de {i} até {f} ', end='', flush=True)
    if p == 0:
        p = 1
        print(f'de {p} em {p}:')
    else:
        print(f'de {p} em {p}:')
    if f < i:
        if p > 0:
            p *= -1
        f -= 1
    else:
        f += 1
    for i in range(i, f, p):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-' * 45)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

