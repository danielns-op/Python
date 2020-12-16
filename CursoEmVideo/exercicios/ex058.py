from time import sleep
from random import randint
print('#' * 12)
print('{:#^12}'.format(' Adivinha '))
print('#' * 12)
print('Estou pensando em um número de 0 á 10.')
print('Tente adivinhar o número que estou pensando...')
sleep(2)
bot = randint(0, 10)
quant = 0
while True:
    num = int(input("Qual número estou pensando: "))
    quant += 1
    if num == bot:
        print('Você disse {} e eu pensei {} ...'.format(num, bot))
        sleep(1)
        print('Você acertou! Você deu {} palpites.'.format(quant))
        break
    else:
        print('Errou, tente novamente...')
        sleep(1)
