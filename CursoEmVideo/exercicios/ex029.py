v = float(input('Velocidade do carro: '))
if v > 80.0:
    multa = (v - 80) * 7
    print("Você foi multado!")
    print("Valor da multa: R$ {:.2f}".format(multa))
else:
    print('Velocidade dentro do limite permitido.')
