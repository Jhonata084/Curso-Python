distância = float(input('Digite a distância km/h: '))
if distância <= 200:
    print(f'Você pagará R${distância * 0.5} pelo preço da passagem')
else:
    print(f'Você pagará R${distância * 0.45} pelo preço da passagem')
