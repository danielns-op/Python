# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os em um dicionário se por acaso a CTPS for diferente de zero,
# o dicionário recebrá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

ano_atual = date.today().year

dados = {'Nome': str(input('Nome: ')),
         'Idade': 0,
         'CTPS': 0}
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = idade = ano_atual - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    ano_aposentar = 92 - idade
    dados['Aposentaduria'] = ano_aposentar
    print('-' * 30)
    for k, v in dados.items():
        if k == 'Salário':
            print(f'{k}: R$ {v:.2f}')
        else:
            print(f'{k}: {v}')
else:
    print('-' * 30)
    for k, v in dados.items():
        print(f'{k}: {v}')
