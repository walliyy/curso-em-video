# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
soma = 0
for c in range(0, 6):
    n = int(input(f'Informe o {c}º valor: '))
    if n % 2 == 0:
        soma += n
print(soma)
print('FIM')