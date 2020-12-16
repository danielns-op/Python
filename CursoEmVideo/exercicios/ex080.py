numeros = []

for n in range(1, 6):
    numero = int(input('Informe um número: '))
    if n == 1:
        numeros.append(numero)
        print(f'Número {numero} adicionado ao final da lista')
    else:
        if numero >= max(numeros):
            numeros.append(numero)
            print(f'Número {numero} adicionado ao final da lista.')
        elif numero < min(numeros):
            numeros.insert(0, numero)
            print(f'Número {numero} adicionado na posição 0 da lista.')
        else:
            for pos, valor in enumerate(numeros):
                if valor < numero < numeros[pos + 1]:
                    numeros.insert(pos + 1, numero)
                    print(f'O número {numero} foi adicionado na posição {pos + 1} da lista')

print(f'Você adicionou os números: {numeros}')
