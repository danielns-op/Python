# Crie um programa que leia nome, sexo e idade de várias pessoas guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) A média de idade do grupo.
#   C) Uma lista com todas as mulheres.
#   D) Uma lista com todas as pessoas com idade acima da média

from time import sleep

lista_dados = []
dados = {}
mulheres = []
idade_acima_media = []

while True:
    dados = {'Nome': str(input('Nome: ')).strip(),
             'Sexo': str(),
             'Idade': int(input('Idade: '))}
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        print('Erro! Digite apenas M - Masculino ou F - Feminino.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    dados['Sexo'] = sexo
    lista_dados.append(dados)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        sleep(0.5)
        break

print('-' * 40)
print(f'- Foram cadastradas {len(lista_dados)} pessoas.')
sleep(0.5)
soma = media = 0

for itens in lista_dados:
    for k, v in itens.items():
        if k == 'Idade':
            soma += v
        if k == 'Sexo' and v == 'F':
            mulheres.append(itens['Nome'])

media = soma / len(lista_dados)
print(f'- A média de idade do grupo é: {media:.0f} anos.')
sleep(0.5)
print(f'- Mulheres cadastradas: ', end='')
for m in mulheres:
    print(f'{m} ', end='')
sleep(0.5)
print(f'\n- Pessoas com idade acima da média:')
for pessoas in lista_dados:
    if pessoas['Idade'] > media:
        print('\t', end='')
        for k, v in pessoas.items():
            print(f'{k} = {v}; ', end='')
        sleep(0.5)
        print('')
print('<<', ' ENCERRADO ', '>>')
