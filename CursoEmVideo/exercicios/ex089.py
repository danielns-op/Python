# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
from time import sleep

lista = []
nome = []
notas = []
media = 0
quant_alunos_cadastrados = 0

while True:
    nome.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    nome.append(notas[:])
    nome.append(media)
    lista.append(nome[:])
    quant_alunos_cadastrados += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    else:
        nome.clear()
        notas.clear()

print('-' * 30)
print(f'{"Nº":<3}{"NOME":<20}{"MÉDIA":^8}')
print('-' * 30)
for dados in lista:
    print(f'{lista.index(dados):<3}{dados[0]:<20}{dados[2]:^8.1f}')
print('-' * 30)

while True:
    escolha = int(input('Mostrar notas de qual aluno? [999 - sair]: '))
    if escolha == 999:
        print('<<< Saindo >>>')
        sleep(1)
        break
    else:
        print(f'Notas de {lista[escolha][0]} são {lista[escolha][1]}')
