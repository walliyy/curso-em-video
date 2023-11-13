# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o número inicial: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao # calculo enesimo termo da PA

while decimo >= primeiro:
    print(primeiro, end=' -> ')
    primeiro += razao
print('ACABOU')