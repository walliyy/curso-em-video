# Escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milimetros
metros = float(input('Informe a metragem: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('Metros: {} \nQuilometros: {} \nHM: {} \nDAM: {} \nDM: {} \nCentimetros: {} \nMilimetros: {}'.format(metros, km, hm, dam, dm, cm, mm))