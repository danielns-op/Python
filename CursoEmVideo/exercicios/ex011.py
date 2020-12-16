largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = altura * largura
tinta = area / 2

print('A parede tem {}m² e será necessário {:.2f} litros de tinta.'.format(area, tinta))
