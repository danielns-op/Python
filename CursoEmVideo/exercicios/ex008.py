m = float(input('Informe um valor em metros: '))

print('A medida de {}m corresponde a:'.format(m))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m / 1000,
                                                   m / 100,
                                                   m / 10,
                                                   m * 10,
                                                   m * 100,
                                                   m * 1000))
