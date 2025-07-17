soma = 0
media = 0
maioridadehomem = 0
nomevelho = ' '
totalmulher20 = 0

for pessoas in range(1, 5):
	print(f'{pessoas}° pessoa')
	nome = str(input('Nome: '))
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).strip()
	soma += idade 
	if pessoas == 1 and sexo in 'Mm':
		maioridadehomem = idade
		nomevelho = nome 
	if sexo in 'Mm' and idade > maioridadehomem:
		maioridadehomem = idade 
		nomevelho = nome 
	if sexo in 'Ff' and idade < 20:
		totalmulher20 += 1
media = soma / 4 
print(f'A média é de {media}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos ')
