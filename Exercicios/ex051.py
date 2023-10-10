# Desenolva um programa que leia o primeiro termo e a razão de uma pa. No final mostre os 1- primeiros termos dessa progressão.
n = int(input('Digite o número inicial: '))
r = int(input('Digite a razão: '))

t = n

for c in range(0, 10):
    print(t)
    t += r

# Solução do professor
primeiro = int(input('Digite o número inicial: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao # calcuilo enesimo termo da PA

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU')