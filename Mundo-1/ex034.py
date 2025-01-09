salario = float(input('Digite o seu salário e vou dizer o valor do aumento: R$ '))
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100) # Vai fazer o aumento de 15%
else:
    aumento = salario + (salario * 10 / 100)
    print(f'Você ganhava {salario:.2f} e vai começar a ganhar {aumento:.2f}')