salário = float(input('Qual o salário do funcionário? R$'))
aumento = salário  + (salário * 15 / 100)
print('O salário antes era de {}, agora com os 15% de aumento ficou {:.2f}'.format(salário, aumento))