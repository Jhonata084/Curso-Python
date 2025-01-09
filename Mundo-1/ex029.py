velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade!')
    multa = (velocidade-80) * 7
    print('Por ter ultrapassado o limite de velocidade, você terá que pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia. Dirija com segurança.') # Esse comando sempre será executado, pois está ao lado esquerdo do programa.
