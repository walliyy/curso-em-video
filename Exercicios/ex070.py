''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato.'''
total = 0.00
maisDeMil = cont = 0
maisBarato = ''
vlrMaisBarato = 0

while True:
    produto = str(input('Informe o produto: '))
    valor = float(input('Informe o valor do item: R$ '))
    if valor > 1000:
        maisDeMil += 1
    if cont <= 1 or valor < vlrMaisBarato:
        maisBarato = produto
        vlrMaisBarato = valor
    # elif valor < vlrMaisBarato:
    #     maisBarato = produto
    #     vlrMaisBarato = valor
    total += valor
    cont += 1
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'sSnN':
        op = str(input('Opção inválida! Deseja continuar? [S/N] ')).upper().strip()[0]
    if op in 'nN':
        break
print('{:-^40}'.format(' FIM DA COMPRA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maisDeMil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato é "{maisBarato}" e ele custa R${vlrMaisBarato:.2f}.')