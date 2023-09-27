# Crie um programa que leia um mnumero Real qualquer pelo teclado e mostre na tela a porção inteira. Ex: Digite um número: 6.127 O numero 6.127 tem a parte inteira 6
from math import trunc

n = float(input('Digite um valor real qualquer: '))

print('O número digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))

# n = float(input('Digite um valor real qualquer: '))

# print('O número digitado foi {} e sua porção inteira é {}'.format(n, int(n)))