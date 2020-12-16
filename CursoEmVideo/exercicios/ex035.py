a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

if a + b < c or a + c < b or c + b < a:
    print('Não pode ser um triangulo.')
else:
    print('Pode ser um triangulo.')
