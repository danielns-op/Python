# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou
# o maior número no dado.
from random import randint
from time import sleep

dados = {}

for n in range(1, 5):
    dados[f'Jogador{n}'] = randint(1, 6)

print('Valores sorteados:')
sleep(1)
for k, v in dados.items():
    print(f'\tO {k} tirou {v}')
    sleep(0.5)

print(f'\nRanking dos Jogadores:')
sleep(1)
posicao = 1
while len(dados) > 0:
    maior = 0
    jogador = {}
    for k, v in dados.items():
        if v > maior:
            maior = v
            jogador = k
    print(f'\t{posicao}º Lugar: {jogador} com {maior}')
    sleep(0.5)
    del dados[jogador]
    posicao += 1

# Na resolução do Guanabara ele utiliza o modulo itemgetter
# from operator import itemgetter
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

