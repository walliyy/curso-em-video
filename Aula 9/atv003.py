# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex: Digite o numero: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1'

# numero = str(input('Informe um numero entre 0 e 0000: '))

# print('Unidade:', numero[3])
# print('Dezena:', numero[2])
# print('Centena:', numero[1])
# print('Milhar:', numero[0])

# Tratando com matematica
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))