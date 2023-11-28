# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex.: 5! 5x4x3x2x1 = 120
num = int(input('Informe o número: '))
cont = num
fatorial = 1
print(f'Calculando fatorial {num}! = ')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end ='')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}')