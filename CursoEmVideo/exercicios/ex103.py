#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha diso informado corretamente.


def ficha(nome, gols=0):
    if not nome:
        nome = '<desconhecido>' 
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 40)
jogador = str(input('Nome do Jogador: ')).strip()
try:
    quant_gol = int(input('Número de Gols: '))
except:
    quant_gol = 0

ficha(jogador, quant_gol)

