velocidade = int(input('Qual é a velocidade do veiculo? '))
if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('Você foi multado! Pois estava dirigindo há {} Km/h, em uma via na qual a velocidade maxima permitida é de 80 Km/h.'.format(velocidade))
    print('O valor da multa a ser paga é de R$ {:.2f}.'.format(valor_multa))
else:
    print('Muito bem! Você está dentro da velocidade permitida na via.')
