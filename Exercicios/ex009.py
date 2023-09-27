# Faça um programa que leia um numero intetiro qualquer e mostre na tela a sua tabuada
num = int(input('Digite um numero inteiro: '))
cont = 1

while cont < 11:
    r = num * cont
    print('{:<2} * {:>2} = {:>2}'.format(num, cont, r))
    cont += 1
