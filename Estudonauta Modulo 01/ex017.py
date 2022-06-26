from math import hypot
cateto_oposto = float(input('Qual o tamanho do cateto oposto?: '))
cateto_adjacente = float(input('Qual o tamanho do cateto adjacente?: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print('O tamanho da hipotenusa deste triangulo retângulo é de {:.2f}'.format(hipotenusa))