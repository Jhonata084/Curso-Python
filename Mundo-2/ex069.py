homens_cadastrados = mulheres = totmaior = 0
while True:
	print('-' *30)
	print('Cadastre uma pessoa')
	print('-' *30)
	idade = int(input('Idade: '))
	sexo = str(input('Sexo: [M/F]')).upper()
	continuar = str(input('Quer continuar? [S/N] ')).upper()
	if sexo not in 'MF':
		print('Informações inválidas, por favor tente novamente ')
	if continuar not in 'SN':
		print('Informações inválidas, por favor tente novamente')
	if idade >= 18:
		totmaior +=1 
	if sexo == 'M':
		homens_cadastrados +=1 
	if idade < 20 and sexo == 'F':
		mulheres +=1
	if continuar == 'N':
		break 
print(f'Total de pessoas com mais de 18 anos: {totmaior}')
print(f'Ao todo temos {homens_cadastrados} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
