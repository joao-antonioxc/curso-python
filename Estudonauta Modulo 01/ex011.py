altura = float(input('Quantos metros a parede tem de altura? '))
largura = float(input('Quantos metros a parede tem de largura? '))
area = altura * largura
litros = area / 2
print('Uma parede com {} metros de altura, e {} metros de largura, possui uma área de {} metros quadrados. Logo irá precisar de {:.1f} litros de tinta para pinta-la.'.format(altura, largura, area, litros))