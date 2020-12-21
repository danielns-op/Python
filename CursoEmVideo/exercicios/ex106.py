#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um mini-sistema que utiliza o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando
# o usuário digitar a palavra 'FIM', o programa se encerrará.
# Obs: use cores.
from time import sleep

amarelo = '\033[1;37;43m'
azul = '\033[1;37;44m'
vermelho = '\033[1;37;41m'
branco = '\033[7;37;40m'
normal = '\033[m'


def apresentacao(texto, cor):
    for c in texto:
        print(f'{cor}~{normal}', end='')

    print(f'\n{cor}{texto}{normal}')

    for c in texto:
        print(f'{cor}~{normal}', end='')
    print('')


def pyhelp():
    while True:
        titulo = ' SISTEMA DE AJUDA PyHELP '
        apresentacao(titulo, amarelo)

        funcao = input('Função ou Biblioteca > ').strip().lower()
        mostrar = f' Acessando o manual do comando {funcao} '

        if funcao == 'fim':
            sair = ' ATÉ LOGO! '
            apresentacao(sair, vermelho)
            sleep(2)
            break
        else:
            apresentacao(mostrar, azul)
            sleep(1.5)
            print(f'{branco}', end='')
            help(funcao)
            print(f'{normal}', end='')
            sleep(3)


pyhelp()

