#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma novas pessoa e listar
# todas as pessoas cadastradas.

from ex115 import cadastros
from time import sleep

amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
azul = '\033[1;34m'
normal = '\033[m'

while True:
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    
    print(f'{amarelo}1{normal} - {azul}Ver pessoas cadastradas{normal}')
    print(f'{amarelo}2{normal} - {azul}Cadastrar nova pessoa{normal}')
    print(f'{amarelo}3{normal} - {azul}Sair do sistema{normal}')
    print('-' * 40)

    opcao = str(input(f'{amarelo}Sua Opção:{normal} ')).strip()

    if opcao == '1':
        cadastros.consulta()
    elif opcao == '2':
        cadastros.cadastro()
    elif opcao == '3':
        break
    else:
        print(f'{vermelho}ERRO: Opção inválida!{normal}')


print('-' * 40)
print('Saindo do sistema... Até logo!')
print('-' * 40)
sleep (2)

