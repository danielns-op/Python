from random import randint
from time import sleep

print('Eu pensei em um número de 1 a 5.')
n = int(input('Tente adivinhar: '))
print('Analisando...')
sleep(1.5)
sorteio = randint(1, 5)
if n == sorteio:
    print("Você acertou!")
else:
    print('Errou, eu pensei no número {}.'.format(sorteio))
