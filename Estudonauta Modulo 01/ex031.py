km_rodado = int(input('Qual a distância total da viajem em Km? '))
if km_rodado <= 200:
    valor_viajem = float(km_rodado * .5)
else:
    valor_viajem = float(km_rodado * .45)
print('O valor da viajem será de R$ {:.2f}'.format(valor_viajem))
