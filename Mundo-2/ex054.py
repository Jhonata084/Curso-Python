from datetime import date
data_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range (1, 8):
	nascimento = int(input(f'Em que ano a {pessoa}° nasceu? '))
	idade = data_atual - nascimento
	if idade >= 21:
		total_maior += 1
	else:
		total_menor += 1
print(f'Ao todo teve {total_maior} pessoas maiores de idade')
print(f'Ao todo teve {total_menor} pessoas menores de idade')
