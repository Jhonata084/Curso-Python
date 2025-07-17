from random import randint
vitorias = 0
print('-' *30)
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('-' *30)
while True:
	jogador = int(input('Digite um valor: '))
	computador = randint(0, 10)
	soma = jogador + computador 
	pi = ' '
	while pi not in 'PI':
		pi = str(input('Par ou Ímpar? [P/I]')).upper()
		print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
		print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
	if pi == 'P':
		if soma % 2 == 0:
			print('VOCÊ GANHOU!!')
			v += 1
		else:
			print('VOCÊ PERDEU!!')
			break 
	elif pi == 'I':
		if soma % 2 == 1:
			print('VOCÊ GANHOU!!')
			v += 1
		else:
			print('VOCÊ PERDEU!!')
print(f'GAME OVER! Você venceu {v} vezes. ')
