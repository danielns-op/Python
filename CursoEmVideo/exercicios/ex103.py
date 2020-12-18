#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha diso informado corretamente.


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 40)
jogador = str(input('Nome do Jogador: '))
quant_gol = int(input('Número de Gols: '))
ficha(jogador, quant_gol)

