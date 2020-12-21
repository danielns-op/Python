#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indica o número a calcular e o outro
# chamado show, que será um valor lógico (opicional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    print('-' * 40)
    fator = 1 
    l_fator = []
    if show:
        print(n, end=' ')
        for c in range(1, n):
            print('x', end=' ')
            fator *= n
            n -= 1
            print(n, end=' ')
        print('=', end=' ')
    else:
        for c in range(1, n):
            fator *= n
            n -= 1
    return fator


print(fatorial(5, show=True))
print('-' * 40)

