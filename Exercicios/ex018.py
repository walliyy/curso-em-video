# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import radians, sin, cos, tan

n = int(input('Informe o valor do angulo: '))
seno = sin(radians(n))
coss = cos(radians(n))
tang = tan(radians(n))
print('O seno de {} é {:.2f}'.format(n, seno))
print('O coseno de {} é {:.2f}'.format(n, coss))
print('A tangente de {} é {:.2f}'.format(n, tang))

# print('Para o grau {}º \nO valor em radianos é {} \nO seno é {} \nO cosseno é {} \nA tangente é {}'.format(n, math.sin(math.radians(n)), math.radians(n), math.cos(math.radians(n)), math.tan(math.radians(n))))