# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.
peso = []
for c in range(1,6):
    peso.append((float(input('Digite seu peso: '))))
print(f'O maior peso é {max(peso)}')
print(f'O menor peso é {min(peso)}')
print(peso)

# Solução do professor
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa : '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}KG')
print(f'O menor peso lido foi de {menor}KG')