# Faça um programa que ajude um jogador da Mega Sena
# a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.
from random import randint

lista = []
quantidade = int(input('Quantos Jogos serão criados: '))

for quant in range(0, quantidade):
    lista.insert(quant, list())
    for num in range(0, 6):
        numero = randint(1, 60)
        lista[quant].append(numero)

print(lista)
