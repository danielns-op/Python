# Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do
# programa, mostre.

# a média de idade do grupo
# qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

idades = 0
mais_velho = 0
nome_mais_velho = ''
quant_mulher_menor = 0

for pessoas in range(1, 5):
    print('{:-^20}'.format('Dados {}ª Pessoa'.format(pessoas)))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idades += idade
    sexo = str(input('Sexo [M/F]: '))
    print('-' * 20)
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        quant_mulher_menor += 1

print('A média de idade do grupo é: {} anos.'.format(idades / 4))
print('O homem mais velho é o {} com {} anos.'.format(nome_mais_velho, mais_velho))
print('No grupo há {} mulheres com menos de 20 anos.'.format(quant_mulher_menor))
