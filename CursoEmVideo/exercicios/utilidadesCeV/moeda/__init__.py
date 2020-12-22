#!/usr/bin/env python
# -*- coding: utf-8 -*-


def aumentar(v, p, f=False):
    """
    --> aumentar(v, p, f=False)
    :param v:
    :param p:
    :param f:
:return:
    """
    aumento = (v * p) / 100
    if f:
        return moeda(v + aumento)
    else:
        return v + aumento


def diminuir(v, p, f=False):
    """
    --> diminuir(v, p, f=False)
    :param v:
    :param p:
    :param f:
    :return:
    """
    diminui = (v * p) / 100
    if f:
        return moeda(v - diminui)
    else:
        return v - diminui


def dobro(v, f=False):
    """
    --> dobro(v, f=False)
    :param v:
    :param f:
    :return:
    """
    if f:
        return moeda(v * 2)
    else:
        return v * 2


def metade(v, f=False):
    """
    --> metade(v, f=False)
    :param v:
    :param f:
    :return:
    """
    if f:
        return moeda(v / 2)
    else:
        return v / 2


def moeda(v):
    """
    --> moeda(v)
    :param v:
    :return:
    """
    return f'R$ {v:.2f}'.replace('.', ',')


def resumo(v, a, d):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(v):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(v, True):<10}')
    print(f'{"Metade do preço:":<20}{metade(v, True):<10}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(v, a, True):<10}')
    print(f'{f"{d}% de redução:":<20}{diminuir(v, d, True):<10}')
    print('-' * 30)
