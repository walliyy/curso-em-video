# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$ '))

novoPreco = preco - (preco*5/100)
print('O novo preço do produto é R$ {:.2f}'.format(novoPreco))