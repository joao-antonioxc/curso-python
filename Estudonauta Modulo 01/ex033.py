n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 < n2:
    if n1 < n3:
        menor_numero = n1
    else:
        menor_numero = n3
else:
    if n2 < n3:
        menor_numero = n2
    else:
        menor_numero = n3
if n1 > n2:
    if n1 > n3:
        maior_numero = n1
    else:
        maior_numero = n3
else:
    if n2 > n3:
        maior_numero = n2
    else:
        maior_numero = n3
print('O menor número que você digitou foi o número {}.'.format(menor_numero))
print('O maior número que você digitou foi o número {}.'.format(maior_numero))
