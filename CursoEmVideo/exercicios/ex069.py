from time import sleep

contador = maior_idade = conta_homens = conta_mulheres = 0

while True:
    nome = str(input('Nome da pessoa: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip()
    contador += 1
    if idade > 18:
        maior_idade += 1
    if sexo in 'Mm':
        conta_homens += 1
    if sexo in 'Ff' and idade < 20:
        conta_mulheres += 1
    pergunta = str(input('Deseja continuar [S/N]: '))
    while pergunta not in 'SsNn':
        pergunta = str(input('Deseja continuar [S/N]: '))
    if pergunta in 'Nn':
        break
    sleep(0.5)

print(f'''
Foram cadastrada {contador} pessoas.
Com os dados informados nos temos:
{maior_idade} pessoa(s) com mais de 18 anos.
{conta_homens} homen(s) cadastrados.
{conta_mulheres} mulher(es) com menos de 20 anos.''')
