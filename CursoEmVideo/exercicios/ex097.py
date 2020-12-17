#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.
# Ex:
#   escreva('Olá, mundo!')
# Saída:
#   ~~~~~~~~~~~
#   Olá, Mundo!
#   ~~~~~~~~~~~

def escreva(texto):
    tam = len(texto)
    print('~' * tam)
    print(f'{texto}')
    print('~' * tam)


escreva('Daniel Noronha')
escreva('Python é TOP!')
escreva('Python')

