print('=' * 30)
print('BANCO DO BRASIL')
print('=' * 30)
saque = int(input('Qual o valor do saque? R$'))
total = saque 
cedulas = 50
total_cedulas = 0
while True:
	if total >= cedulas:
		total -= cedulas 
		total_cedulas += 1
	else:
		if total_cedulas > 0:
			print(f'Total de {total_cedulas} cedulas de R${cedulas}')
		if cedulas== 50:
			cedulas = 20
		elif cedulas == 20:
			cedulas = 10
		elif cedulas == 10:
			cedulas = 1
		total_cedulas = 0
		if total == 0:
			break
print('=' * 30)
print('Volte sempre ao BANCO DO BRASIL!')
		