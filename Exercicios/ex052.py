# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
n = int(input('Digite um numero: '))
tot = 0
for c in range(2, n-1):
    if n % c == 0:
        tot += 1
    c += 1
if tot == 0:
    print('É primo')
else:
    print('Não é primo')