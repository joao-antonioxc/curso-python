km = int(input('Quantos Km o veículo percorreu? '))
dias = int(input('Quantos dias o veículo foi alugado? '))
print('Como o veículo percorreu {} Km, e foi alugado por {} dias. O total a pagar é de R$ {}.'.format(km, dias, ((km * .15) + (dias * 60))))
