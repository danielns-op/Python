# Faça um programa que ajude um jogador da Mega Sena
# a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.
from random import randint
from time import sleep

print('-' * 30)
print(f'{"Palpites MEGA SENA":^30}')
print('-' * 30)

lista = []
numeros = []
quantidade = int(input('Quantos Jogos serão criados: '))

for quant in range(0, quantidade):
    for num in range(0, 6):
        numero = randint(1, 60)
        while numero in numeros:
            numero = randint(1, 60)
        numeros.append(numero)
    lista.append(numeros[:])
    numeros.clear()

print(f'{f" Sorteando {quantidade} JOGOS ":-^30}')
for valores in lista:
    valores.sort()
    print(f'Jogo {lista.index(valores) + 1}: {valores}')
    sleep(1)
print(f'{" BOA SORTE! ":-^30}')
