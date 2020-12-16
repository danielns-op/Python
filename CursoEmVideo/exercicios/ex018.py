from math import sin, cos, tan, radians
a = float(input('Informe um ângulo: '))
seno = sin(radians(a))
cose = cos(radians(a))
tang = tan(radians(a))

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cose, tang))
