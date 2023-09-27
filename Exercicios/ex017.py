# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o compromimento da hipotenusa.
from math import hypot

co = float(input('Informa o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hy = hypot(co, ca)
# hy = (co ** 2 + ca ** 2) ** (1/2)

print('Cateto oposto: {} \nCateto adjacente: {} \nHipotenusa: {:.2f}'.format(co, ca, hy))