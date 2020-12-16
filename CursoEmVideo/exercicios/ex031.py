d = float(input('Distância da viagem em km: '))

if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45

print('Preço da passagem: R$ {:.2f}'.format(p))
