from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10, quer tentar adivinhar qual foi?')
acertou = False 
tentativas = 0
while not acertou:
	jogador = int(input('Qual número você escolhe?'))
	tentativas += 1
	if jogador == computador:
		acertou = True 
	else:
		if jogador < computador:
			print('Mais... tente novamente')
		elif jogador > computador:
			print('Menos... tente novamente')
print(f'Acertou com {tentativas} tentativas')
