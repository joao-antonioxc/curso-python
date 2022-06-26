preco = float(input('Qual o preço do produto? R$ '))
desconto = 5 / 100
valor_desconto = preco * desconto
novo_preco = preco - valor_desconto
print('O produto com preço R$ {:.2f}, aplicando o desconto {:.2f}%, tem R$ {:.2f} de desconto. Logo seu novo preço é de R$ {:.2f}.'.format(preco, (desconto * 100), valor_desconto, novo_preco))
