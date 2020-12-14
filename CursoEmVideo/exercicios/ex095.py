# Aprimore o DESAFIO 093 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.
from time import sleep

db_jogadores = {}

print(f'{"Análise Tática":-^40}')
cont = 1
while True:
    print('-' * 40)
    dados_jogador = {'Nome': str(input('Nome do jogador: ')).strip(),
                     'Partidas': int(input('Partidas jogadas: ')),
                     'Gols': [],
                     'Total de Gols': 0}

    for p in range(1, dados_jogador['Partidas'] + 1):
        gols = int(input(f'O Jogador {dados_jogador["Nome"]} fez quantos gols na {p}ª partida: '))
        dados_jogador['Gols'].append(gols)
        dados_jogador['Total de Gols'] += gols

    db_jogadores[f'Jogador_{cont}'] = dados_jogador.copy()
    dados_jogador.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        print('-' * 40)
        break
    else:
        cont += 1

while True:
    print('-' * 40)
    print(f'{"COD":<5}{"Nome":<15}{"Gols":<25}{"Total":<5}')
    cod = 0
    for valor in db_jogadores.values():
        cod += 1
        print(f'{cod:<5}{valor["Nome"]:<15}{valor["Gols"]}{" ":>10}{valor["Total de Gols"]:<5}')
    print('-' * 40)
    visualizar = int(input('Visualizar dados de qual jogador [COD]: '))
    while visualizar > len(db_jogadores):
        print(f'Favor informar um número entre 1 e {len(db_jogadores)}.')
        visualizar = int(input('Visualizar dados de qual jogador [COD]: '))

print('-' * 40)
#sleep(1)

#for k, v in dados_jogador.items():
#    print(f'{k}: {v}')
#print('-' * 40)
#sleep(1)

#print(f'O Jogador {dados_jogador["Nome"]} jogou {dados_jogador["Partidas"]} partidas.')
#for pos, quant in enumerate(dados_jogador['Gols']):
#    print(f'\t=> Na partida {pos + 1}, {dados_jogador["Nome"]} fez {quant} gols.')
#print(f'Foi um total de {dados_jogador["Total de Gols"]} gols.')
#print('-' * 40)
