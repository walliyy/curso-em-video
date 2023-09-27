# Escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milimetros
metros = float(input('Informe a metragem: '))

cent = metros * 100
mili = metros * 1000

print('Metros: {} \nCentimetros: {} \nMilimetros: {}'.format(metros, cent, mili))