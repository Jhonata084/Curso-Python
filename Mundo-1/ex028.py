from random import randint # Faz o computador sortear um número
from time import sleep # Faz o computador "dormir" por alguns segundos, ou que está processando, ou está "pensando"
computador = randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar em qual eu pensei...')
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) # O computador vai ficar 3 segundos "Pensando"
if jogador == computador:
    print('PARABENS, você me venceu')
else:
    print('ERRADO, eu não pensei no número {} e sim no {}'.format(jogador, computador))
