from random import randint
palavras = ('Pedra', 'Papel', 'Tesoura')
sorteio = randint(0, 2)

print('''Suas opções:
 [ 0 ] Pedra
 [ 1 ] Papel
 [ 2 ] Tesoura''')

jogador = int(input('Qual você escolhe? '))
print(f'Computador jogou {palavras[sorteio]}')
print(f'Jogador jogou {palavras[jogador]}')

if sorteio == 0 and jogador == 0:
	print('Empate!')
elif sorteio == 1 and jogador == 1:
	print('Empate!')
elif sorteio == 2 and jogador == 2:
	print('Empate!')
elif sorteio == 3 and jogador == 2:
	print('Empate!')
	
elif jogador == 0 and sorteio == 1:
	print('Você perdeu!')
elif jogador == 1 and sorteio == 2:
	print('Você perdeu!')
elif jogador == 2 and sorteio == 0:
	print('Você perdeu!')
	
elif jogador == 0 and sorteio == 2:
	print('Você ganhou!')
elif jogador == 1 and sorteio == 0:
	print('Você ganhou!')
elif jogador == 2 and sorteio == 1:
	print('Você ganhou!')
	