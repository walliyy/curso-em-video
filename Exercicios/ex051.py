# Desenolva um programa que leia o primeiro termo e a razão de uma pa. No final mostre os 1- primeiros termos dessa progressão.
n = int(input('Digite o número inicial: '))
r = int(input('Digite a razão: '))

t = n

for c in range(0, 10):
    print(t)
    t += r