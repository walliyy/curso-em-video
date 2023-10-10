# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print('É primo')
else:
    print('Não é primo')

# Solução do professor
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')