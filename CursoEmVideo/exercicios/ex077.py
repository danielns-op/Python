palavras = ('Amor', 'Felicidade', 'Paz', 'Tranquilidade', 'Paixao')

for palavra in palavras:
    print(f'A Palavra {palavra} possuí as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(f'{letra} ', end='')
    print('')
