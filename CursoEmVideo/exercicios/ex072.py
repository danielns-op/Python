numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Escolha um número de 0 á 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente. Escolha um número de 0 á 20: '))

for pos, numero in enumerate(numeros):
    if pos == num:
        print(f'Você escolheu o número "{numero}"')
