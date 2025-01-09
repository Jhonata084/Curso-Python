dia = int(input('Quantos dias você passou com o carro? '))
km = float(input('Quantos Km você percorreu com o carro? '))
res = (dia * 60) + (km * 0.15)
print('O valor a ser pago é {:.2f}R$'. format(res))