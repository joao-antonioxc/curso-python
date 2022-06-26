n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2) # ou pow(n, (1/2))
print('O dobro é {}, o triplo é {}, e a raiz quadrada de {} é {:.3f}'.format(d, t, n, pow(n, (1/2))))
