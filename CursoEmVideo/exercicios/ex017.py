from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto Adjascente: '))

print('Hipotenusa: {:.2f}'.format(hypot(co, ca)))
