num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
	if num % c == 0:
		print('\033[m')
		total +=1
	else:
		print('\033[31m')
	print(f'{c}')
if total == 2:
	print(f'O número {num} é PRIMO!')	
else:
	print(f'O número {num} NÃO É PRIMO!')
	