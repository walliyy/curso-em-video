# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex.: 5! 5x4x3x2x1 = 120
n1 = n2 = int(input('Informe o número: '))
contador = 0
tot = 0

while n1 != 0:
    n1 -= 1
    tot = n2 * n1
    print(f'{n2} x {n1} = ', end='')
    print(tot)    
# for c in range(n, 0, -1):
#     print2(c, end='x')
#     fat = n * c
#     n = c
#     print(n)
#     print(fat)
# print(fat)