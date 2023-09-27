# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kilometros foram rodados? '))

valor = (dias * 60) + (km * 0.15)
print('O valor a pagar é de R${:.2f}'.format(valor))