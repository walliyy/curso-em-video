# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o número inicial: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao # calcuilo enesimo termo da PA

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU')
while primeiro <= decimo + razao: