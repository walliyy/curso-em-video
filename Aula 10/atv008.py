# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

maior = n1
n4 = n2
n5 = n3

if (n2 > maior):
    maior = n2
    n4 = n1
    n5 = n3
if (n3 > maior):
    maior = n3
    n4 = n1
    n5 = n2

soma = n4 + n5

if maior >= soma:
    print('Não forma triangulo!')
else:    
    print('Forma triangulo!')

# solução do professor
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
# verificando se é um triângulo]
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma triangulo!')
else:
    print('Não forma triangulo!')