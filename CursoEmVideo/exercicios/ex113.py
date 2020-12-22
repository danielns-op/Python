#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveitando e crie também uma função
# leiaFloat() com a mesma
from time import sleep


def leiaInt(texto):
    while True:
        try:
            valor = int(input(texto))
            if valor:
                break
        except KeyboardInterrupt:
            print('\033[1;33mO usuário preferiu não informar os dados!\033[m')
            valor = 0
            break
        except:
            print('\033[1;31mERRO: Digite um número inteiro válido!\033[m')
            sleep(1)

    return valor        


def leiaFloat(texto):
    while True:
        try:
            valor = float(input(texto))
            if valor:
                break
        except KeyboardInterrupt:
            print('\033[1;33mO usuário preferiu não informar os dados!\033[m')
            valor = 0
            break
        except:
            print('\033[1;31mERRO: Digite um número real válido!\033[m')
            sleep(1)

    return valor if valor == 0 else f'{valor:.2f}'


num_int = leiaInt('Digite um número Inteiro: ')
num_rel = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {num_int} e o real foi {num_rel}.')

    
