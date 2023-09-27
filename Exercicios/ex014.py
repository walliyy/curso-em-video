# Faça um algoritmo que leia a temperatura em graus Cº e converta ela para Fº
c = float(input('Informe a temperatura em graus Cº: '))
f = 9 * c / 5 + 32
print('A tempetaruta de {}°C corresponde a {}Fº!'.format(c, f))