# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Digite o valor que possui em dinheiro: ')) 
conversao = 3.27

dolar = real / conversao

print('Com R${:.2f} você consegue comprar US${:.2f} que esta na cotação atual de R${:.2f}'.format(real, dolar, conversao))

