#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico.
# Ex:
#   n = leiaInt('Digite um n')
from time import sleep


def leiaInt(texto):
    valor = input(texto)
    while True:
        if valor.isnumeric():
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            sleep(1)
            valor = input(texto)
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

