print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0 
mais = 10
while mais != 0:
	total = total + mais 
	while cont <= total:
		print(f'{termo} - ', end='')
		termo += razao 
		cont += 1
	print('Pausa')
	mais = int(input('Quantos termos você quer adicionar? '))
print(f'Progressão finalizada com {total} termos')
