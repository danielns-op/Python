from random import randint

numeros = ('',)
maior_numero = 0
menor_numero = 0

for valor in range(1, 6):
    numero = (randint(1, 10),)
    numeros += numero
    if valor == 1:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero


print(f'Tupla gerada: {numeros[1:]}')
print(f'Maior número: {maior_numero[0]}')
print(f'Menor número: {menor_numero[0]}')
