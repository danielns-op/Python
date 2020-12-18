# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números
# e vai colocálos dentro da lista e a segunda função vai mostrara soma
# entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

numeros = []


def sorteia():
    print('Sorteando 5 valores para a lista:', end=' ', flush=True)
    for n in range(0, 5):
        sleep(0.5)
        valor = randint(1, 10)
        numeros.append(valor)
        print(valor, end=' ', flush=True)
    print('PRONTO!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {numeros},', end=' ', flush=True)
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    sleep(1)
    print(f'temos {soma}.')


sorteia()
somaPar()
