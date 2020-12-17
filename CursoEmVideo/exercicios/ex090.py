# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

dados = {}
nome = str(input('Nome do aluno: '))
media = float(input(f'Média de {nome}: '))
dados['Nome'] = nome
dados['Média'] = media

for k, v in dados.items():
    print(f'{k} é igual a {v}')

if dados['Média'] >= 7:
    print('Situação é igual a Aprovado.')
elif dados['Média'] >= 5:
    print('Situação é igual a Recuperação.')
else:
    print('Situação é igual a Reprovado.')
