# Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 < n1 and n2 > n3:
        print('{} é o MAIOR e {} é o MENOR'.format(n1, n3))
    elif n2 < n1 and n2 < n3:
        print('{} é o MAIOR e {} é o MENOR'.format(n1, n2))
elif n2 > n1 and n2 > n3:
    if n1 < n2 and n1 > n3:
        print('{} é o MAIOR e {} é o MENOR'.format(n2, n3))
    elif n1 < n2 and n1 < n3:
        print('{} é o MAIOR e {} é o MENOR'.format(n2, n1))
elif n3 > n1 and n3 > n2:
    if n1 < n3 and n1 > n2:
        print('{} é o MAIOR e {} é o MENOR'.format(n3, n2))
    elif n1 < n3 and n1 < n2:
        print('{} é o MAIOR e {} é o MENOR'.format(n3, n1))

# solução do professor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# verificando menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3