# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.
peso = []
for c in range(1,6):
    peso.append((float)(input('Digite seu peso: ')))
print(f'O maior peso é {max(peso)}')
print(f'O menor peso é {min(peso)}')
print(peso)