nome = str(input('Nome completo: '))

print('Nome maiúsculo:\n{}'.format(nome.upper()))
print('Nome minúsculo:\n{}'.format(nome.lower()))
nl = len(nome) - nome.count(' ')
print('Quantas letras ao todo sem espaços:\n{}'.format(nl))
tn = nome.split()
print('Quantas letras tem o primeiro nome:\n{}'.format(len(tn[0])))
