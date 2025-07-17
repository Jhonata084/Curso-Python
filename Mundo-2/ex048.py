soma = 0
contador = 0
for cont in range(1, 501, 2):
	if cont % 3 == 0:
		contador = contador + 1 # contador += 1
		soma = soma + cont # soma += c
print(f'A soma de todos os {contador} valores é {soma}')