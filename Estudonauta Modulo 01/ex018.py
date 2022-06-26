from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo {}, possui seno {:.3f}, cosseno {:.3f} e tangente {:.3f}.'.format(angulo, seno, cosseno, tangente))
