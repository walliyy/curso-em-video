# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: '))

novoPreco = preco - (preco*0.05)
print('O novo preço do produto é R$ {:.2f}'.format(novoPreco))