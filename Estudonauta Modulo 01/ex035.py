r1 = int(input('Digite qual o tamanho da primeira reta: '))
r2 = int(input('Digite qual o tamanho da segunda reta: '))
r3 = int(input('Digite qual o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Sim é possível fazer um triângulo com as 3 medida.')
else:
    print('Não é possível fazer um triângulo com as 3 medidas.')
# testando
