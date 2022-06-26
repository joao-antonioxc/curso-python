n = int(input('Qual tabuada deseja? '))
print('-'*18)
for i in range(10):
    print('{:^4} x {:^4} = {:^4}'.format(n, (i + 1), (n * (i + 1))))
print('-'*18)
