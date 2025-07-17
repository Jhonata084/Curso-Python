total = totalmil = menor = cont = 0
barato = ' '
print('-' *30)
print('SUPERMERCADO BARATÃO')
print('-' *30)
while True:
	produto = str(input('Nome do produto: '))
	valor = float(input('Valor do produto: R$'))
	cont += 1 
	total += valor
	if valor > 1000:
		totalmil += 1 
	if cont == 1 or valor < menor:
		menor = valor 
		barato = produto
	res = str(input('Quer continuar? [S/N]')).upper()
	if res == 'N':
		break 
print('FIM DO PROGRAMA')
print(f'O total da compra foi {total}')
print(f'Temos {totalmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato}, custando R${menor}')
