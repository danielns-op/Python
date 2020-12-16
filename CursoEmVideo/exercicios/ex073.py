times = ('Atlético-MG', 'São Paulo', 'Flamengo', 'Internacional', 'Palmeiras',
         'Santos', 'Grêmio', 'Fluminense', 'Fortaleza', 'Corinthians', 'Ceará',
         'Athletico', 'Bahia', 'Atlético-GO', 'RB Bragantino', 'Sport', 'Vasco',
         'Coritiba', 'Botafogo', 'Goiás')

posFort = 0
timeFor = 'Fortaleza'

# Minha primeira versão
print('Lista dos 5 primeiros e 4 últimos do brasileirão serie A 2020.')
for pos, time in enumerate(times):
    if pos < 5:
        print(f'{pos + 1} - {time}')
    if pos > 15:
        print(f'{pos +1} - {time}')
    if time == timeFor:
        posFort = pos + 1

print(f'\n{sorted(times)}')
print(f'\nO time {timeFor} está na posição {posFort}.\n\n')

print('-' * 40)

# Abaixo segue minha versão após vê a execução do programa do professor.
cinco_primeiro = ('',)
quatro_ultimos = ('',)

for pos in range(0, len(times)):
    if pos < 5:
        time = (times[pos],)
        cinco_primeiro += time
    if pos > 15:
        time = (times[pos],)
        quatro_ultimos += time
    if times[pos] == timeFor:
        posFort = pos + 1

print('-=' * 20)
print(f'Lista dos 20 primeiros times do Brasileirão serie A - 2020.')
print(times)
print('-=' * 20)
print(f'Lista dos 5 primeiros:')
print(cinco_primeiro[1:])
print('-=' * 20)
print(f'Lista dos 4 últimos:')
print(quatro_ultimos[1:])
print('-=' * 20)
print('Lista completa em ordem Alfabética:')
print(sorted(times))
print('-=' * 20)
print(f'O time {timeFor} está na posição {posFort}.')
print('-=' * 20)

print('-' * 40)

# Segue minha versão de forma otimizada.
print('-=' * 20)
print(f'Lista dos 20 primeiros times do Brasileirão serie A - 2020')
print(times)
print('-=' * 20)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-=' * 20)
print(f'Os quatros últimos colocados: {times[-4:]}')
print('-=' * 20)
print('Times por ordem Alfabética:')
print(sorted(times))
print('-=' * 20)
print(f'Posição do time fortaleza: {times.index("Fortaleza") + 1}')
print('-=' * 20)
