# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
num = int(input('Digite um numero inteiro: '))

antecessor = num - 1
sucessor = num + 1

print('O numero digitado é {}, o antecessor desse numero é {} e o sucessor desse numero é {}'.format(num, antecessor, sucessor))