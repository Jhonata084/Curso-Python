compras = float(input('Qual o valor das compras? R$'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))

if opcao == 1:
	resultado = 10 / 100 * compras 
	print(f'Sua compra de {compras}, vai custar {compras - resultado} no final.')
elif opcao == 2:
	resultado2 = 5 / 100 * compras 
	print(f'Sua compra de {compras:.2f}, vai custar {compras - resultado2:.2f} no final.')
elif opcao == 3:
	print('Vai custar o preço normal.')
elif opcao == 4:
	resultado3 = compras + (compras *20 / 100)
	resultado4 = 20 / 100 * compras
	parcelas = int(input('Quantas parcelas? '))
	print(f'Sua compra será parcelada em {parcelas}x de {resultado3 / parcelas:.2f} com juros.')
	print(f'Sua compra de R${compras:.2f} vai custar {compras + resultado4:.2f} no final.')
