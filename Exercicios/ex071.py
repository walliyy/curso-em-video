# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS. Considerando que o caixa possui cedulas de R% 50, R$20, R$10 e R$1.
valor_original = int(input('Informe o valor do saque: '))
valor = valor_original
notas50 = notas20 = notas10 = notas1 = 0
while True:
    if valor >= 50:
        notas50 +=1
        valor -= 50
    elif valor >= 20:
        notas20 += 1
        valor -= 20
    elif valor >= 10:
        notas10 += 1
        valor -= 10
    elif valor >= 1:
        notas1 += 1
        valor -= 1
    else:
        break
print(f'Para efetuar o saque de R$ {valor_original}, você irá receber', end=' ')
if notas50 > 0:
    print(f'{notas50} notas de R$ 50,00,', end=' ')
if notas20 > 0:   
    print(f'{notas20} notas de R$ 20,00,', end=' ')
if notas10 > 0:
    print(f'{notas10} notas de R$ 10,00,', end=' ')
if notas1 > 0:
    print(f'{notas1} notas de R$ 1,00,', end=' ')
print(f'totalizando o saldo solicitado.')



# valor = float(input('Informe o valor do saque: '))
# cedulasUm = cedulasDez = cedulasVinte = cedulasCinquenta = 0
# cedulasCinquenta = valor // 50
# restoCinquenta = valor % 50
# if restoCinquenta > 20:
#     cedulasVinte = restoCinquenta // 20
#     restoVinte = restoCinquenta % 20
# elif restoCinquenta > 10:
#     cedulasDez = restoCinquenta // 10
#     restoDez = restoCinquenta % 10
# elif restoCinquenta > 1:
#     cedulasUm = restoCinquenta // 1
#     restoUm = restoCinquenta % 1

# print(f'cedulas 50 {cedulasCinquenta}')
# print(f'resto 50 {restoCinquenta}')
# print(f'cedulas 20 {cedulasVinte}')
# print(f'resto 20 {restoVinte}')
# print(f'cedulas 10 {cedulasDez}')
# print(f'resto 10 {restoDez}')
# print(f'cedulas 1 {cedulasUm}')
# print(f'resto 1 {restoUm}')