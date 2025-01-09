a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a
menor = a

# Verifica qual o maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Verifica qual o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
if maior == menor: # Verifica se os números possuem o mesmo valor 
    print('Os números possuem o mesmo valor')
else:
    print(f'O maior número é o {maior}')
    print(f'O menor número é o {menor}')
    