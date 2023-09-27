# Faça um programa que leia a largura e altura de uma parede em metros, calcue a sua área e a quantidade de tinta necessária para pintála, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
media = 2.0

area = largura * altura
tinta = area/media
print('Sua parede tem {}m x {}m e sua área é de {}m², para pintar essa area serão necessários {}L de tinta'.format(largura, altura, area, tinta))