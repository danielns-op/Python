#!/usr/bin/env python
# -*- coding: utf-8 -*-


def leiaDinheiro(texto):
    vermelho = '\033[1;31m'
    normal = '\033[m'

    while True:
        valor = str(input(texto)).strip()
        if '.' in valor:
            nvalor = valor.replace('.', '')
            if nvalor.isnumeric():
                valor = float(valor)
                break
        elif ',' in valor:
            nvalor = valor.replace(',', '')
            if nvalor.isnumeric():
                valor = valor.replace(',', '.')
                valor = float(valor)
                break
        elif not valor.isnumeric():
            print(f'{vermelho}ERRO: \"{valor}\" é um preço inválido!{normal}')
        else:
            valor = float(valor)
            break

    return valor

