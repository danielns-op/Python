#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um código em Python que teste se o site Pudim está
# acessível pelo computador usado.
import socket


def verificaSite(site, porta=80):
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #site = 'https://www.pudim.com.br'
    conexao.settimeout(0.5)
    try:
        teste = conexao.connect_ex((site, porta))
        if teste == 0:  # ok, acessível.
            return f'\033[1;33mConsegui acessar o site \"{site}\" com sucesso!\033[m'
    except:
        return f'\033[1;31mO site \"{site}\" não está acessível no momento.\033[m'


site = str(input('Qual site: '))

acesso = verificaSite(site)

print(acesso)

