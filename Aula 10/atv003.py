# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
num = int(input('Digite o número: '))
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))