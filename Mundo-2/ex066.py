soma = numd = 0
while True:
	num = int(input('Digite um número inteiro (999 para parar): '))
	if num == 999:
		break
	soma += num 
	numd += 1
print(f'Ao todo foram digitados {numd} números e a soma entre eles é {soma}')
