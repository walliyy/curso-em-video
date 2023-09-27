'''Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/pix: 10% de deconto
- a vista cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAO DO BÃO '))
preco = int(input('Preço das compras: R$'))
cond = int(input('Selecione a condição de pagamento: \n'
                 '1 - A vista (Dinheiro/PIX) \n'
                 '2 - A vista Cartão \n'
                 '3 - Até 2x no Cartão \n'
                 '4 - 3x ou mais no Cartão \n'))
if cond == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco - (preco * 0.10)))
elif cond == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco - (preco * 0.05)))
elif cond == 3:
    print('O valor a ser pago é de R$ {:.2f}'.format(preco))
elif cond == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preco + (preco * 0.20)
    print('O valor a ser pago é de R$ {:.2f} '
          'dividido em {}x de {:.2f}'.format(juros, parcelas, (juros / parcelas)))
else:
    print('Forma de pagamento inválida!')