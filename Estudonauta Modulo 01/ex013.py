salario = float(input('Qual o salário do funcionário? R$ '))
porc_aumento = 15 / 100
aumento = salario * porc_aumento
novo_salario = salario + aumento
print('Um funcionário com salário R$ {:.2f}, após receber um aumento de {:.0f}%, terá um acréscimo de R$ {:.2f}, logo ele irá receber R$ {:.2f} de salário.'.format(salario, porc_aumento * 100, aumento, novo_salario))
