from time import sleep
from random import randint

print('-=' * 10)
print('{:^20}'.format('Par ou Ímpar?'))
print('=-' * 10)

jogador = ''
quantidade_vitorias = 0
while True:
    jogador = str(input('''
    Qual sua opção?
        [ 1 ] - Par
        [ 2 ] - Ímpar
    opção: ''')).strip()
    if jogador == '1' or jogador == '2':
        sleep(0.5)
    else:
        print('Opção inválida.')
        sleep(0.5)
        continue
    numero_jogador = str(input('Qual seu número [de 0 á 10]: '))
    if int(numero_jogador) in range(1, 11):
        sleep(0.5)
    else:
        print('Valores fora do intervalo solicitado.')
        sleep(1)
        continue
    numero_bot = randint(0, 10)
    soma = int(numero_jogador) + numero_bot
    if jogador == '1':
        escolha_jogador = '[Par]'
        bot, escolha_bot = 2, '[Ímpar]'
    else:
        escolha_jogador = '[Ímpar]'
        bot, escolha_bot = 1, '[Par]'
    print(f'>> Você pediu {escolha_jogador} número [{numero_jogador}].')
    sleep(0.5)
    print(f'>> Eu pedi {escolha_bot} número [{numero_bot}].')
    sleep(0.5)
    print(f'[{numero_jogador}] + [{numero_bot}] = [{soma}]')
    sleep(0.5)
    if soma % 2 == 0 and jogador == '1':
        print(f'O número [{soma}] é par...')
        print('Você Venceu!!')
        quantidade_vitorias += 1
        sleep(1)
    elif soma % 2 != 0 and jogador == '2':
        print(f'O número [{soma}] é ímpar...')
        print('Você venceu!!')
        quantidade_vitorias += 1
    else:
        print('Eu venci, tchau perdedor!')
        break

print(f'Você teve um total de {quantidade_vitorias} vitória(s) consecultiva(s).')
