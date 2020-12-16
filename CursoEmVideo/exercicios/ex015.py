d = int(input('Dias alugados: '))
k = float(input('Kilometros utilizados: '))

t = (0.15 * k) + (60 * d)

print('Total a pagar: R$ {:.2f}'.format(t))
