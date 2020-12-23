#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
# todas as pessoas.
from time import sleep

# cores
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
azul = '\033[1;34m'
verde = '\033[1;32m'
normal = '\033[m'

# nome do arquivo/DB com as informações de cadastro.
arquivo = './ex115/DBcadastros.db'

def cadastro():
    print('-' * 40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' * 40)

    nome = str(input(f'{amarelo}Nome:{normal} ')).strip()
    
    while True:
        try:
            idade = int(input(f'{amarelo}Idade:{normal} '))
            break
        except ValueError:
            print(f'{vermelho}ERRO: Por Favor, digite um número inteiro válido.{normal}')
            sleep(1)

    gravar = open(arquivo, 'a')
    gravar.write(f'{nome:<30}{f"{idade} anos":<10}\n')
    gravar.close()
    print(f'{azul}{nome} {verde}cadastrado com sucesso!{normal}')
    sleep(2)


def consulta():
    try:
        ler = open(arquivo, 'r')
        print(f'{verde}Acessando arquivo...{normal}')
        sleep(1)
    except:
        print(f'{amarelo}Arquivo não existe, criando arquivo...{normal}')
        open(arquivo, 'x')
        sleep(1)
        print(f'{verde}Arquivo: {azul}\"{arquivo}\" {verde}criado com sucesso!{normal}')
        ler = open(arquivo, 'r')
        sleep(1)
    
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)

    print(ler.read())
    ler.close()
    sleep(3)

