numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Escolha um número de 0 á 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Escolha um número de 0 á 20: '))

for pos, numero in enumerate(numeros):
    if pos == num:
        print(f'Você escolheu o número "{numero}"')

# Desafio para refazer o mesmo conteúdo adicionando um questionamento
# ate o usuário pedir para sair.
print('\nDESAFIO!\n')

while True:
    num = int(input('Escolha um número de 0 á 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente. Escolha um número de 0 á 20: '))
    print(f'Você escolheu o número "{numeros[num]}"')
    continuar = str(input(f'\nDeseja continuar [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    if continuar == 'S':
        continue
