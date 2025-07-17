from time import sleep
primeirov = int(input('Primeiro valor: '))
segundov = int(input('Segundo valor: '))

while True:
	print(" [ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa")
	opcao = int(input('Qual a sua opção?'))
	if opcao == 1:
		print(f'A soma dos números digitados é {primeirov + segundov}')
	elif opcao == 2:
		print(f'A multiplicação dos números digitados é {primeirov * segundov}')
	elif opcao == 3:
		if primeirov > segundov:
			print(f'O maior número entre os digitados foi o {primeirov}')
		elif segundov > primeirov:
	 	  print(f'O maior número entre os digitados foi o {segundov}')
	elif opcao == 4:
		print('Informe os valores novamente: ')
		primeirov = int(input('Primeiro valor: '))
		segundov = int(input('Segundo valor: '))
	elif opcao == 5:
		print('Finalizando...')
		sleep(3)
		break
	else:
		print('Opção inválida, tente novamente.')
	sleep(2)
print('Fim do programa, volte sempre!!')
