#!/usr/bin/env python
# -*- coding: utf-8 -*-


def aumentar(v, p, f=False):
    aumento = (v * p) / 100
    if f:
        return moeda(v + aumento)
    else:
        return v + aumento


def diminuir(v, p, f=False):
    diminui = (v * p) / 100
    if f:
        return moeda(v - diminui)
    else:
        return v - diminui


def dobro(v, f=False):
    if f:
        return moeda(v * 2)
    else:
        return v * 2


def metade(v, f=False):
    if f:
        return moeda(v / 2)
    else:
        return v / 2


def moeda(v):
    return f'R$ {v:.2f}'.replace('.', ',')

