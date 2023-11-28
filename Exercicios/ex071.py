# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS. Considerando que o caixa possui cedulas de R% 50, R$20, R$10 e R$1.
valor = float(input('Informe o valor do saque: '))
cedulasUm = cedulasDez = cedulasVinte = cedulasCinquenta = 0
cedulasCinquenta = valor // 50
restoCinquenta = valor % 50
if restoCinquenta > 20:
    cedulasVinte = restoCinquenta // 20
    restoVinte = restoCinquenta % 20
elif restoCinquenta > 10:
    cedulasDez = restoCinquenta // 10
    restoDez = restoCinquenta % 10
elif restoCinquenta > 1:
    cedulasUm = restoCinquenta // 1
    restoUm = restoCinquenta % 1

print(f'cedulas 50 {cedulasCinquenta}')
print(f'resto 50 {restoCinquenta}')
print(f'cedulas 20 {cedulasVinte}')
print(f'resto 20 {restoVinte}')
print(f'cedulas 10 {cedulasDez}')
print(f'resto 10 {restoDez}')
print(f'cedulas 1 {cedulasUm}')
print(f'resto 1 {restoUm}')