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

