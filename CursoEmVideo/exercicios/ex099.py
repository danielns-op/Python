# Faça um programa que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual
# deles é o maior.
from time import sleep

def maior(*valor):
    n_maior = 0
    print('-' * 45)
    print(f'Analisando os valores passados...', flush=True)
    sleep(0.5)
    for v in valor:
        print(v, end=' ', flush=True)
        sleep(0.5)
        if v > n_maior:
            n_maior = v
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi o {n_maior}.', flush=True)
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
