retaA = float(input('Comprimento reta A: '))
retaB = float(input('Comprimento reta B: '))
retaC = float(input('Comprimento reta C: '))

triang = ''

if retaA >= (retaB + retaC):
    print('Não pode ser um triângulo.')
    print('A reta A: {}, é maior que a soma das retas B e C'.format(retaA))
    print('\treta B: {} + reta C: {} = {}'.format(retaB, retaC, (retaB + retaC)))
elif retaB >= (retaA + retaC):
    print('Não pode ser um triângulo.')
    print('A reta B: {}, é maior que a soma das retas A e C.'.format(retaB))
    print('\treta A: {} + reta C: {} = {}'.format(retaA, retaC, (retaA + retaC)))
elif retaC >= (retaA + retaB):
    print('Não pode ser um triângulo.')
    print('A reta C: {}, é maior que a soma das retas A e B.'.format(retaC))
    print('\treta A: {} + reta B: {} = {}'.format(retaA, retaB, (retaA + retaB)))
else:
    print('As retas formão um trinângulo:')
    if retaA != retaB != retaC != retaA:
        triang = 'Escaleno.'
    if retaA == retaB != retaC or retaA == retaC != retaB:
        triang = 'Isósceles.'
    if retaB == retaA != retaC or retaB == retaC != retaA:
        triang = 'Isósceles.'
    if retaC == retaA != retaB or retaC == retaB != retaA:
        triang = 'Isósceles.'
    if retaA == retaB == retaC:
        triang = 'Equilátero.'
    print('\t{}'.format(triang))
