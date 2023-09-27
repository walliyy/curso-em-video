# Desenvolva um programa que pergunte a distancia de uma viagem e m KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km e R$0,45 para viagens mais longas.
d = float(input('Informe a distancia da viagem: '))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('Para viajar a distancia de {:.2f}KM, o custo total da viagem será de R${:.2f}'.format(d, p))    

# resolução professor
dist = float(input('Informe a distancia da viagem: '))
preco = dist * 0.50 if dist <= 200 else dist * 0.45