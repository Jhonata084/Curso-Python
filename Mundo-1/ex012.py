preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto está na promoção, com desconto de 5%,  ficando {:.2f} '.format(novo))