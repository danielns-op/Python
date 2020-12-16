# JokenPo
#  Autor: Daniel Noronha
# e-mail: danielnoronha.sh@gmail.com
#   date: 18/11/2020

from random import randint
from time import sleep
from os import system

CAMAP = '\033[1;5;33m'
CAMAN = '\033[1;33m'
CVERN = '\033[1;31m'
CVEDN = '\033[1;32m'
CAZUN = '\033[1;34m'
CCIAN = '\033[1;36m'
CNORM = '\033[m'


def carregando():
    sleep(1)
    system('clear')
    print(f'{CAMAN}carregando')
    sleep(1)
    system('clear')
    print('carregando.')
    sleep(1)
    system('clear')
    print('carregando..')
    sleep(1)
    system('clear')
    print(f'carregando...{CNORM}')
    sleep(1.5)


def jogo():
    while True:
        system('clear')
        print(f'{CAMAP}BEM VINDO AO JOKENPO!!!{CNORM}')
        print(f'{CCIAN}JOGADOR: {CAZUN}{njoga}{CCIAN}')
        opcao = str(input('''\tEscolha:
        \t\t1 - Pedra   [@]
        \t\t2 - Papel   [|]
        \t\t3 - Tesoura [V]
        \tOpção:{} '''.format(CVEDN)))
        sorteiopc = randint(0, 2)
        listapc = ['Pedra [@]', 'Papel [|]', 'Tesoura [V]']
        oppc = listapc[sorteiopc]

        if opcao == '1':
            escolhajogador = 'Pedra [@]'
            if oppc == escolhajogador:
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAN}Empate!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Papel [|]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAP}PC venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Tesoura [V]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CVEDN}{njoga} Venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
        elif opcao == '2':
            escolhajogador = 'Papel [|]'
            if oppc == escolhajogador:
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAN}Empate!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Tesoura [V]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAP}PC venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Pedra [@]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CVEDN}{njoga} Venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
        elif opcao == '3':
            escolhajogador = 'Tesoura [V]'
            if oppc == escolhajogador:
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAN}Empate!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Pedra [@]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CAMAP}PC venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
            if oppc == 'Papel [|]':
                print(f'{CAZUN}{njoga}{CCIAN}: {CVEDN}{escolhajogador}{CNORM}')
                print(f'{CAZUN}PC{CCIAN}: {CVEDN}{oppc}{CNORM}')
                print(f'{CVEDN}{njoga} Venceu!!!{CNORM}')
                novamente = str(input('Jogar novamente [s/N]: '))
                if novamente in 'Ss':
                    continue
                else:
                    exit(0)
        else:
            print(f'{CVERN}Opção inválida.{CNORM}')
            sleep(2)
            continue


# Execução
system('clear')
print(f'{CAMAN}BEM VINDO AO JOKENPO!!!{CNORM}')
njoga = str(input(f'{CCIAN}Nome do jogador:{CAZUN} '))
print(f'{njoga}{CCIAN} vamos jogar!!!{CNORM}')
sleep(1)
carregando()
jogo()
