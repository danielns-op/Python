#!/usr/bin/env python
# -*- coding: utf-8 -*-


def leiaDinheiro(texto):
    vermelho = '\033[1;31m'
    normal = '\033[m'
    while True:
        valor = str(input(texto)).strip()
        if not valor.isnumeric():
            print(f'{vermelho}ERRO: \"{valor}\" é um preço inválido!{normal}')
        else:
            if ',' in valor:
                valor = valor.replace(',', '.')
            break
    return valor

