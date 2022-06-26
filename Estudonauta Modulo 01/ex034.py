salario = float(input('Qual o valor do seu salário? R$ '))
if salario > 1250:
    print('Você terá um aumento de 10% logo seu novo salário será de R$ {:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print('Você terá um aumento de 15% logo seu novo salário será de R$ {:.2f}'.format(salario + (salario * 15 / 100)))
