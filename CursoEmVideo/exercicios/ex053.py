frase = str(input('Qual a frase: ')).strip()

formfrase = frase.lower().replace(' ', '')

contador = len(formfrase) - 1

for letra in range(len(formfrase)):
    if formfrase[letra] != formfrase[contador]:
        exit('Não é um Palíndromo.')
    contador -= 1

print('A frase "{}" é um Palíndromo!'.format(frase))
