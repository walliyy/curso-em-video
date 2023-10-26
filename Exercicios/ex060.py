# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex.: 5! 5x4x3x2x1 = 120
n = fat = int(input('Informe o número: '))
contador = 0
tot = 0

while fat != 0:
    tot = n * (fat-1)
    n -= 1
    fat == n
    print(n)
print(tot)
# for c in range(n, 0, -1):
#     print(c, end='x')
#     fat = n * c
#     n = c
#     print(n)
#     print(fat)
# print(fat)