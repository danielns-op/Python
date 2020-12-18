#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date

ano_atual = date.today().year


def voto(ano):
    idade = ano_atual - ano
    if idade >= 18 and idade < 65:
        status = 'OBRIGATÓRIO'
    elif idade < 18:
        status = 'NÃO VOTA'
    else:
        status = 'OPCIONAL'
    return f'Com {idade} anos: {status}.'


nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))

