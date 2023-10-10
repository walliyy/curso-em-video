# Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 até 500
s = 0
for c in range (1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            s += c
print(s)

# Solução do professor

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')