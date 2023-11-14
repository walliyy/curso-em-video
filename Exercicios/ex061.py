# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o número inicial da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao # calculo enesimo termo da PA

while decimo >= primeiro:
    print(primeiro, end=' -> ')
    primeiro += razao
print('ACABOU')

# Solução do professor
first = int(input('Digite o número inicial da PA: '))
raz = int(input('Digite a razão da PA: '))
termo = first
cont = 1

while cont <= 10:
    print(termo, end=' -> ')
    termo += raz
    cont += 1
print('ACABOU')