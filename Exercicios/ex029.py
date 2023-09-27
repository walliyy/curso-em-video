# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite.
km = float(input('Informe a velocidade do veiculo: '))

if km > 80:
    v = (km - 80) * 7
    print('Você foi multado! O valor da multa é de R${:.2f}'.format(v))
print('Tenha um bom dia. Dirija em segurança!')