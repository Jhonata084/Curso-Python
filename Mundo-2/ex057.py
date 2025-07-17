while True:
	sexo = str(input('Informe seu sexo: [M/F] ')).upper()
	if sexo == 'M' or sexo == 'F':
		print(f'Sexo {sexo} registrado com sucesso')
		break
	else:
		print('Sexo inválido ')