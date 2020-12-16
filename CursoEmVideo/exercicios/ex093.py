# Crie um programa que gerencie o aproveitamento de um jogo de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.
from time import sleep

print(f'{"Análise Tática":-^40}')
dados_jogador = {'Nome': str(input('Nome do jogador: ')),
                 'Partidas': int(input('Partidas jogadas: ')),
                 'Gols': [],
                 'Total de Gols': 0}

for p in range(1, dados_jogador['Partidas'] + 1):
    gols = int(input(f'O Jogador {dados_jogador["Nome"]} fez quantos gols na {p}ª partida: '))
    dados_jogador['Gols'].append(gols)
    dados_jogador['Total de Gols'] += gols
print('-' * 40)
sleep(1)

for k, v in dados_jogador.items():
    print(f'{k}: {v}')
print('-' * 40)
sleep(1)

print(f'O Jogador {dados_jogador["Nome"]} jogou {dados_jogador["Partidas"]} partidas.')
for pos, quant in enumerate(dados_jogador['Gols']):
    print(f'\t=> Na partida {pos + 1}, {dados_jogador["Nome"]} fez {quant} gols.')
print(f'Foi um total de {dados_jogador["Total de Gols"]} gols.')
print('-' * 40)
