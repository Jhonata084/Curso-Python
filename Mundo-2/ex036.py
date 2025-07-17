casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de {casa:.2f} em {anos} anos, a prestação será de {prestacao:.2f}')

if prestacao <= minimo:
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')
  
