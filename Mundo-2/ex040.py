nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A média entre {nota1} e {nota2}, é igual a {media:.1f}')

if media < 5.0:
   print('Reprovado')
elif media >= 5.0 and media <= 6.9:
   print('Recuperação')
else:
   print('Aprovado')
