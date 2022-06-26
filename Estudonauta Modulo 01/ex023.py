n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade deste número é {}'.format(u))
print('A dezena deste número é {}'.format(d))
print('A centena deste número é {}'.format(c))
print('A milhar deste número é {}'.format(m))