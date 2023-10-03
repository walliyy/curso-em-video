# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.
from datetime import date

menor = 0
maior = 0

for c in range (0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    if (date.today().year - ano) < 21:
        menor += 1
    else:
        maior += 1
print(f'Das 7 pessoas informadas {menor} são menores de idade e {maior} já atingiram a maioridade!')